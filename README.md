# GIS, Forestry, and Remote Sensing Scripting Toolbox

This repository contains a curated collection of Python, R, and Batch scripts used for GIS data processing, point cloud/LiDAR analysis, remote sensing raster operations, and forestry vegetation mapping. 

The toolbox has been organized into logical directories to group similar functionality together, with sequential versions maintained to preserve script development history.

---

## 📂 Repository Structure

The toolbox is organized into the following directories:

*   [📁 raster_processing/](file:///C:/Users/clark/Documents/toolbox/raster_processing) - Scripts for raster format conversions, clipping, extent calculations, and resampling.
    *   [📁 domain_buffer_clip/](file:///C:/Users/clark/Documents/toolbox/raster_processing/domain_buffer_clip) - Sub-scripts for buffering and clipping raster boundaries.
*   [📁 point_cloud_lidar/](file:///C:/Users/clark/Documents/toolbox/point_cloud_lidar) - Point cloud filtering (`.las` files), surface generation, photogrammetric principal point extraction, and LiDAR/Phodar height model comparison.
*   [📁 gis_vector/](file:///C:/Users/clark/Documents/toolbox/gis_vector) - GPS GPX track parsing, shapefile editing, flight line indexing, QGIS-specific actions, and spatial geometry creation.
*   [📁 veg_mapping_classification/](file:///C:/Users/clark/Documents/toolbox/veg_mapping_classification) - Vegetation height, canopy cover classification, random forest predictive models, and separability analysis.
*   [📁 file_utilities/](file:///C:/Users/clark/Documents/toolbox/file_utilities) - Reusable utilities for batch file renaming, file copying from lists, CSV imports, and image compression loops.
*   [📁 miscellaneous/](file:///C:/Users/clark/Documents/toolbox/miscellaneous) - General scripting tools including USGS place name analysis, ASCII art generators, and algorithm tests.
*   [📁 data/](file:///C:/Users/clark/Documents/toolbox/data) - Core CSV list files used by copy and process batch scripts.

---

## 🗃 Detailed Directory & Script Map

### 1. Raster Processing (`raster_processing/`)
Operational tools for manipulation of digital elevation models (DEMs), aerial orthomosaics, and satellite bands.
*   `ascii_to_img_v1.py` & `ascii_to_img_v2.py`: Batch converts ASCII elevation grids (`.asc`) to ERDAS IMAGINE (`.img`) format.
*   `extract_rasters_by_mask.py`: Extracts raster pixels using a vector boundary mask via Spatial Analyst.
*   `resample_naip_imagery.py`: Downgrades NAIP imagery resolution (e.g. by a factor of 10) in target project areas to optimize processing.
*   `landsat_clip.py`: Clips Landsat satellite bands to specified boundaries.
*   `raster_extent_clip_test.py`: Debugging script for raster extent boundary clipping.
*   `batch_write_raster_extents.py`: Iterates through `.tif` files in a folder and saves their bounding box coordinates to a text log.
*   `calculate_raster_buffered_extent.py`: Calculates coordinates for a 300-meter margin inside/outside a raster's extent.
*   `raster_invert_test.py`: Inverts raster values (multiplies by -1) for terrain analysis.
*   `domain_from_raster.py`: Extracts a boundary shapefile showing the valid data extent of a raster.
*   `spectral_indices_calculator.py`: Computes common remote sensing spectral indices (NDVI, NBR, NDWI) from satellite band rasters.

#### 🔸 Raster Domain buffering and clipping (`raster_processing/domain_buffer_clip/`)
Scripts that generate valid data domains for rasters, buffer them inward (e.g., -300 meters) to remove edge noise/null data, and clip the original rasters to this clean boundary.
*   `buffer_v1.py` & `export_clip_v1.py`: Early ModelBuilder-to-Python exports.
*   `domain_buffer_clip_v1.py`: Consolidated script implementing the full domain-buffer-clip workflow for single files.
*   `domain_buffer_clip_v2.py` - `domain_buffer_clip_v3.py`: Batch processing loops iterating over lists.
*   `domain_buffer_clip_v4_trials.py` - `domain_buffer_clip_v7_csv_working.py`: Interactive versions that read input file paths from `rmapList.csv` to safely batch process large volumes.

---

### 2. Point Cloud & LiDAR Processing (`point_cloud_lidar/`)
Tools to work with raw LiDAR (`.las`), photogrammetry block outputs (`.blk`), and canopy height models (CHM).
*   `filter_las_generator_v1.py` - `filter_las_generator_v4_blk3a2.py`: Automates generating Windows batch scripts (`.bat`) to clean and filter noisy `.las` files using the FUSION/LDART `FilterData` CLI.
*   `grid_surface_to_ascii_v1.py` & `grid_surface_to_ascii_v2_test.py`: Automates generating batch scripts to convert gridded LAS point cloud surfaces into ASCII formats.
*   `extract_film_coords_from_blk_v1.py` & `extract_film_coords_from_blk_v2_kaibab.py`: Extracts principal point film-to-image coordinates from photogrammetry `.blk` files by invoking the `hfatest.exe` helper binary.
*   `phodar_lidar_evaluation_v1_ak.R` & `phodar_lidar_evaluation_v2.R`: R scripts that load, plot, and statistically evaluate structural differences between photogrammetry-derived CHMs (Phodar) and active laser sensor CHMs (LiDAR).
*   `fusion_cloudmetrics_generator.py`: Scans a directory for `.las` point clouds and generates batch scripts to calculate canopy and height metrics using USDA Forest Service FUSION CLI tools.

---

### 3. GIS Vector Operations (`gis_vector/`)
Utility scripts focused on editing, creating, and indexing vector features (points, lines, polygons).
*   `gpx_to_shapefile.py`: Batch imports GPS GPX exchange files and outputs ArcGIS-compatible shapefiles.
*   `points_to_line.py`: Converts sequence points (like GPS tracks) to linear polylines.
*   `qgis_geojson_to_shapefile_v1.py` & `qgis_geojson_to_shapefile_v2_batch.py`: Python console snippets for QGIS to convert GeoJSON layer tables in the active canvas directly to ESRI Shapefiles.
*   `flightlines_expnum_test_v1.py` & `flightlines_expnum_test_v2.py`: Extracts unique flight exposure indexes (`EXPNUM`) and projects vector path lines.
*   `big_year_map_creation.py`: Reads bird-watching location CSVs, maps coordinates, finds the minimum bounding envelope (MBR), and creates path maps.
*   `batch_reproject_shapefiles.py`: Batch projects shapefiles in a workspace to a target Coordinate Reference System (CRS) using ArcPy.

---

### 4. Vegetation Mapping & Classification (`veg_mapping_classification/`)
Advanced modeling and statistical workflows for mapping forestry resources, canopy cover, and tree height classes.
*   `veg_class_assignment_carson_v1.py` & `veg_class_assignment_carson_v2.py`: Classification scripts for Carson National Forest. Uses an `UpdateCursor` to assign canopy size classes based on heights and data sources.
*   `veg_class_assignment_santafe_v1.py` - `veg_class_assignment_santafe_v3_cleaned.py`: Similar reclassification scripts tailored for the Santa Fe National Forest dataset.
*   `uwc_separability_analysis.R`: Computes Mahalanobis, Bhattacharyya, and Jeffries-Matusita distances between vegetation classes to analyze spectral separability for the Uinta-Wasatch-Cache National Forest.
*   `vegetation_mapping_random_forest.R`: Trains a Random Forest classifier in R using training plots and applies predictions to map vegetation types.
*   `zonal_stats_rf_classifier.py`: Connects Arcpy spatial zonal stats with Pandas and Geopandas dataframes to format datasets for Dixie National Forest machine learning models.

---

### 5. File & Data Utilities (`file_utilities/`)
Cross-project helper scripts to automate system tasks.
*   `copy_files_from_list_v1.py` & `copy_files_from_list_v2_xml.py`: Reads file paths from CSV indexes (`list.csv`) and batches copying of raw `.tif` or `.xml` metadata scans across system drives.
*   `remove_files_from_list.py`: Reads a CSV index and deletes corresponding files.
*   `rename_files_replace_string_v1.py` & `rename_files_replace_string_v2.py`: Fast filesystem utility to replace strings (like removing `_clip`) across thousands of filenames in less than a second.
*   `import_csv_trial.py`: Testing script for importing tabular CSVs as arcpy rasters.
*   `join_table_and_copy_fields.py`: Joins CSV tables to spatial shapefiles, copy attributes between fields, and cleans up temporary fields.
*   `simulated_copy_workload.py`: Emulates active workload by sleeping random intervals while copying files from a CSV list (useful for pipeline testing).
*   `generate_random_number_arcgis.py`: Python code block expression for the ArcGIS Field Calculator to compute random float values.
*   `compress_tif_batch.bat`: Calls ISRU compression binaries (`mr_file.exe`) to compress `.tif` files into JPEG files with overviews.
*   `uncompress_tif_batch.bat`: Batch uncompresses `.tif` files.

---

## 🛠 Prerequisites and Dependencies

The scripts in this toolbox target different software environments:

1.  **Arcpy Scripts**: Require an active installation of ESRI ArcGIS Desktop (ArcMap) or ArcGIS Pro with Python 2.7 / 3.x, and appropriate extensions (Spatial Analyst, 3D Analyst).
2.  **R Scripts**: Require R with packages `ggplot2`, `plyr`, `geomnet`, `ape`, and `raster`.
3.  **QGIS Scripts**: Executed from inside the QGIS Python Console interface.
4.  **CLI Binaries**: Commands like `FilterData` (FUSION/LDART LiDAR tools) and `mr_file.exe` (ISRU compression) must be present in your system path or hardcoded paths updated.
