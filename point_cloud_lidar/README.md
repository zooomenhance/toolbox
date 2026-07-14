# LiDAR & Point Cloud Processing Toolset

This directory contains R, Python, and Batch scripts to clean, process, and analyze active LiDAR (`.las`) data and photogrammetric surface height models.

## 📄 Scripts

### Point Cloud Cleaning & Filtering
*   **[`filter_las_generator_v1.py`](file:///C:/Users/clark/Documents/toolbox/point_cloud_lidar/filter_las_generator_v1.py) to [`filter_las_generator_v4_blk3a2.py`](file:///C:/Users/clark/Documents/toolbox/point_cloud_lidar/filter_las_generator_v4_blk3a2.py)**:
    *   **Purpose**: Scans directories for `.las` point clouds and generates Windows Batch (`.bat`) command files that call the FUSION/LDART `FilterData` utility. This utility removes high/low outlier noise using standard deviations and window size algorithms.
    *   **Libraries**: `os`.
*   **[`fusion_cloudmetrics_generator.py`](file:///C:/Users/clark/Documents/toolbox/point_cloud_lidar/fusion_cloudmetrics_generator.py)**:
    *   **Purpose**: Scans a folder of `.las` point clouds and generates a Windows Batch (`.bat`) script that runs FUSION's `CloudMetrics` and `GridMetrics` CLI tools to compute forest structure statistics (canopy cover, height percentiles, density).
    *   **Libraries**: `os`.
*   **[`grid_surface_to_ascii_v1.py`](file:///C:/Users/clark/Documents/toolbox/point_cloud_lidar/grid_surface_to_ascii_v1.py) & [`grid_surface_to_ascii_v2_test.py`](file:///C:/Users/clark/Documents/toolbox/point_cloud_lidar/grid_surface_to_ascii_v2_test.py)**:
    *   **Purpose**: Generates batch files to automate converting point cloud grid surfaces to standard ASCII format.
*   **[`canopy_model_bridger_teton_3m.bat`](file:///C:/Users/clark/Documents/toolbox/point_cloud_lidar/canopy_model_bridger_teton_3m.bat)**:
    *   **Purpose**: An example Windows batch script that calls FUSION's `canopymodel` tool to process and generate a 3m canopy height model (CHM) from a folder of `.las` files.

### Photogrammetric Principal Point Extraction
*   **[`extract_film_coords_from_blk_v1.py`](file:///C:/Users/clark/Documents/toolbox/point_cloud_lidar/extract_film_coords_from_blk_v1.py) & [`extract_film_coords_from_blk_v2_kaibab.py`](file:///C:/Users/clark/Documents/toolbox/point_cloud_lidar/extract_film_coords_from_blk_v2_kaibab.py)**:
    *   **Purpose**: Parses photogrammetric camera block files (`.blk`) by executing the `hfatest.exe` utility in a subprocess. It parses the print output to map and export principal point coordinates for each image into a text file.
    *   **Libraries**: `subprocess`.

### Height Model Comparison (R)
*   **[`phodar_lidar_evaluation_v1_ak.R`](file:///C:/Users/clark/Documents/toolbox/point_cloud_lidar/phodar_lidar_evaluation_v1_ak.R) & [`phodar_lidar_evaluation_v2.R`](file:///C:/Users/clark/Documents/toolbox/point_cloud_lidar/phodar_lidar_evaluation_v2.R)**:
    *   **Purpose**: Evaluates spatial and statistical structural differences between photogrammetry-derived CHMs (Phodar) and active laser sensor CHMs (LiDAR). Plots raster correlations and profiles.
    *   **Libraries**: `raster`, `maptools`, `sp`.
