#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Batch Shapefile Reprojector
---------------------------
Scans a folder for shapefiles (`.shp`) and batch reprojects them to a target Coordinate Reference System (CRS).
Useful for preparing coordinate data (such as GPS tracks or imagery polygons) for unified geoprocessing.

Common EPSG Spatial References:
- 4326: WGS 1984 (Standard GPS GCS)
- 26912: NAD 1983 UTM Zone 12N (Common in AZ / Utah)
- 26913: NAD 1983 UTM Zone 13N (Common in NM / Colorado)

Usage:
    python batch_reproject_shapefiles.py --workspace C:/data/shp --epsg 26913
"""

import os
import sys
import argparse

def reproject_shapefiles(workspace, target_epsg):
    """Iterates through all shapefiles in the workspace and reprojects them to the target EPSG code."""
    try:
        import arcpy
        arcpy.env.workspace = workspace
        arcpy.env.overwriteOutput = True
        
        # Check out Spatial Analyst if needed (not strictly required for Project but good practice)
        print(f"Setting target spatial reference to EPSG: {target_epsg}...")
        target_sr = arcpy.SpatialReference(target_epsg)
        
        # List shapefiles
        shapefiles = arcpy.ListFeatureClasses("*.shp")
        if not shapefiles:
            print(f"No shapefiles found in workspace '{workspace}'.")
            return False
            
        print(f"Found {len(shapefiles)} shapefiles to process.")
        
        # Create output directory
        out_dir = os.path.join(workspace, "reprojected")
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
            
        for shp in shapefiles:
            in_path = os.path.join(workspace, shp)
            out_name = f"{os.path.splitext(shp)[0]}_epsg{target_epsg}.shp"
            out_path = os.path.join(out_dir, out_name)
            
            # Check current spatial reference
            desc = arcpy.Describe(shp)
            current_sr = desc.spatialReference
            
            print(f"Projecting '{shp}' (Current: {current_sr.name}) -> '{out_name}'...")
            
            # Run projection geoprocessor
            # Syntax: Project_management (in_dataset, out_dataset, out_coor_system, {transform_method}, {in_coor_system}, {preserve_shape})
            arcpy.Project_management(in_path, out_path, target_sr)
            
        print(f"Success: Reprojected shapefiles saved to '{out_dir}'")
        return True
        
    except ImportError:
        print("Error: ArcPy not found. This script requires an ArcGIS python environment.")
        return False
    except Exception as e:
        print(f"Geoprocessing error: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Batch Reproject Shapefiles using ArcPy")
    parser.add_argument("--workspace", required=True, help="Path to directory containing input shapefiles.")
    parser.add_argument("--epsg", type=int, required=True, 
                        help="Target EPSG coordinate reference system code (e.g. 4326 for WGS84, 26913 for UTM 13N).")
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.workspace):
        print(f"Error: Workspace '{args.workspace}' is not a valid directory.")
        sys.exit(1)
        
    success = reproject_shapefiles(args.workspace, args.epsg)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
