# Raster Processing Toolset

This folder contains Python scripts for processing spatial raster datasets (orthophotos, satellite imagery, and DEMs), primarily utilizing the `arcpy` geoprocessing library.

## 📂 Subdirectories

*   **[`domain_buffer_clip/`](file:///C:/Users/clark/Documents/toolbox/raster_processing/domain_buffer_clip)**: Contains versioned scripts implementing a boundary-buffering pipeline that extracts valid raster domains, shrinks them slightly (negative buffering), and clips rasters to discard edge interpolation errors.

## 📄 Scripts

### Raster Formatting & Conversion
*   **[`ascii_to_img_v1.py`](file:///C:/Users/clark/Documents/toolbox/raster_processing/ascii_to_img_v1.py) & [`ascii_to_img_v2.py`](file:///C:/Users/clark/Documents/toolbox/raster_processing/ascii_to_img_v2.py)**:
    *   **Purpose**: Batch processes ASCII grid files (`.asc`) to ERDAS IMAGINE format (`.img`).
    *   **Libraries**: `arcpy`, `glob`, `os`.
    *   **Usage**: Update the `filepath` variable to point to your directory of `.asc` files and run the script.
*   **[`spectral_indices_calculator.py`](file:///C:/Users/clark/Documents/toolbox/raster_processing/spectral_indices_calculator.py)**:
    *   **Purpose**: Calculates remote sensing spectral indices (NDVI, NBR, NDWI) from input raster bands, automatically selecting either ArcPy or Rasterio/NumPy depending on the environment.
    *   **Libraries**: `arcpy` (ESRI Spatial Analyst) or `rasterio`/`numpy` (open-source).

### Resampling & Clipping
*   **[`resample_naip_imagery.py`](file:///C:/Users/clark/Documents/toolbox/raster_processing/resample_naip_imagery.py)**:
    *   **Purpose**: Degrades spatial resolution (resamples NAIP quarter quads by a factor of 10) in target project areas to optimize high-throughput processing.
    *   **Libraries**: `arcpy`, `os`.
*   **[`landsat_clip.py`](file:///C:/Users/clark/Documents/toolbox/raster_processing/landsat_clip.py)**:
    *   **Purpose**: Clips Landsat satellite imagery bands to a specified region of interest.
    *   **Libraries**: `arcpy`.
*   **[`extract_rasters_by_mask.py`](file:///C:/Users/clark/Documents/toolbox/raster_processing/extract_rasters_by_mask.py)**:
    *   **Purpose**: Extracts raster subsets using a polygonal mask feature class.
    *   **Libraries**: `arcpy` (Spatial Analyst).

### Extents & Geometry
*   **[`batch_write_raster_extents.py`](file:///C:/Users/clark/Documents/toolbox/raster_processing/batch_write_raster_extents.py)**:
    *   **Purpose**: Scans a directory of `.tif` rasters and writes their bounding box coordinates (XMin, YMin, XMax, YMax) into a text log.
*   **[`calculate_raster_buffered_extent.py`](file:///C:/Users/clark/Documents/toolbox/raster_processing/calculate_raster_buffered_extent.py)**:
    *   **Purpose**: Computes coordinates for a 300-meter inset buffer around a raster's extent.
*   **[`domain_from_raster.py`](file:///C:/Users/clark/Documents/toolbox/raster_processing/domain_from_raster.py)**:
    *   **Purpose**: Runs the `RasterDomain_3d` tool to extract the active vector boundary polygon of an imagery file.
*   **[`raster_invert_test.py`](file:///C:/Users/clark/Documents/toolbox/raster_processing/raster_invert_test.py)**:
    *   **Purpose**: Inverts raster pixel values (multiplying by -1). Used for calculating inverted canopy heights or depth profiles.

### Troubleshooting
*   **[`raster_extent_clip_test.py`](file:///C:/Users/clark/Documents/toolbox/raster_processing/raster_extent_clip_test.py)**:
    *   **Purpose**: Experimental script testing dynamic clipping using extents and geometry.
