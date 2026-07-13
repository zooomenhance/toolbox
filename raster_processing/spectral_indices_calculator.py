#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Spectral Indices Calculator
---------------------------
Calculates common remote sensing spectral indices (NDVI, NBR, NDWI) from raster bands.
Supports both ESRI ArcPy and open-source Rasterio/NumPy environments.

Supported Indices:
- NDVI: (NIR - Red) / (NIR + Red)               [Vegetation Health]
- NBR:  (NIR - SWIR) / (NIR + SWIR)             [Burn Severity]
- NDWI: (Green - NIR) / (Green + NIR)           [Water Features / Moisture]

Usage:
    python spectral_indices_calculator.py --index NDVI --band1 nir.tif --band2 red.tif --output ndvi.tif
"""

import os
import sys
import argparse

def calculate_index_arcpy(band1_path, band2_path, output_path):
    """Calculates Normalized Difference Index using ESRI ArcPy."""
    try:
        import arcpy
        from arcpy.sa import Raster, Float
        arcpy.CheckOutExtension("Spatial")
        
        print("Using ArcPy geoprocessing engine...")
        r1 = Raster(band1_path)
        r2 = Raster(band2_path)
        
        # Cast to Float to avoid integer division truncation
        index = Float(r1 - r2) / Float(r1 + r2)
        index.save(output_path)
        print(f"Success: Saved index raster to {output_path}")
        return True
    except ImportError:
        print("Error: ArcPy not found. Make sure you are running this in an ArcGIS Python environment.")
        return False
    except Exception as e:
        print(f"Error during ArcPy calculations: {e}")
        return False

def calculate_index_rasterio(band1_path, band2_path, output_path):
    """Calculates Normalized Difference Index using Rasterio and NumPy."""
    try:
        import rasterio
        import numpy as np
        
        print("Using Rasterio/NumPy processing engine...")
        with rasterio.open(band1_path) as src1, rasterio.open(band2_path) as src2:
            meta = src1.meta.copy()
            meta.update(dtype=rasterio.float32, count=1)
            
            arr1 = src1.read(1).astype(np.float32)
            arr2 = src2.read(1).astype(np.float32)
            
            # Suppress divide-by-zero warnings
            with np.errstate(divide='ignore', invalid='ignore'):
                index = (arr1 - arr2) / (arr1 + arr2)
                # Replace NaNs and Infs with a standard NoData value
                index = np.nan_to_num(index, nan=-9999.0, posinf=-9999.0, neginf=-9999.0)
                
            meta.update(nodata=-9999.0)
            
            with rasterio.open(output_path, 'w', **meta) as dst:
                dst.write(index, 1)
        print(f"Success: Saved index raster to {output_path}")
        return True
    except ImportError:
        print("Error: Rasterio or NumPy not found. Install via 'pip install rasterio numpy'.")
        return False
    except Exception as e:
        print(f"Error during Rasterio calculations: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Calculate Remote Sensing Spectral Indices (NDVI, NBR, NDWI).")
    parser.add_argument("--index", choices=["NDVI", "NBR", "NDWI"], required=True, 
                        help="The spectral index to calculate.")
    parser.add_argument("--band1", required=True, help="Path to Band 1 (NIR for NDVI/NBR, Green for NDWI).")
    parser.add_argument("--band2", required=True, help="Path to Band 2 (Red for NDVI, SWIR for NBR, NIR for NDWI).")
    parser.add_argument("--output", required=True, help="Path where the output index raster will be saved.")
    parser.add_argument("--engine", choices=["arcpy", "rasterio", "auto"], default="auto",
                        help="Geoprocessing library to use (default: auto).")
    
    args = parser.parse_args()
    
    # Verify inputs exist
    if not os.path.exists(args.band1) or not os.path.exists(args.band2):
        print("Error: One or both of the input bands do not exist.")
        sys.exit(1)
        
    success = False
    
    if args.engine == "arcpy":
        success = calculate_index_arcpy(args.band1, args.band2, args.output)
    elif args.engine == "rasterio":
        success = calculate_index_rasterio(args.band1, args.band2, args.output)
    else:
        # Auto mode: try ArcPy first, fall back to Rasterio
        try:
            import arcpy
            success = calculate_index_arcpy(args.band1, args.band2, args.output)
        except ImportError:
            success = calculate_index_rasterio(args.band1, args.band2, args.output)
            
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
