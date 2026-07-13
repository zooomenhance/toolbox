# File and Data Utilities

This directory contains cross-project utility scripts that automate tedious filesystem and data formatting tasks.

## 📄 Scripts

### Batch Copying & Removal
*   **[`copy_files_from_list_v1.py`](file:///C:/Users/clark/Documents/toolbox/file_utilities/copy_files_from_list_v1.py) & [`copy_files_from_list_v2_xml.py`](file:///C:/Users/clark/Documents/toolbox/file_utilities/copy_files_from_list_v2_xml.py)**:
    *   **Purpose**: Reads file names from a CSV list (`list.csv`), searches index directories, and batch-copies raw aerial scans (`.tif` or `.aux.xml`) from raw directories to target working directories.
    *   **Libraries**: `csv`, `shutil`, `os`.
*   **[`remove_files_from_list.py`](file:///C:/Users/clark/Documents/toolbox/file_utilities/remove_files_from_list.py)**:
    *   **Purpose**: Reads a CSV list and deletes the corresponding files from a directory to clean up disk space.
    *   **Libraries**: `csv`, `os`.

### Mass Renaming
*   **[`rename_files_replace_string_v1.py`](file:///C:/Users/clark/Documents/toolbox/file_utilities/rename_files_replace_string_v1.py) & [`rename_files_replace_string_v2.py`](file:///C:/Users/clark/Documents/toolbox/file_utilities/rename_files_replace_string_v2.py)**:
    *   **Purpose**: Replaces sub-strings (such as removing `_clip`) in file names across thousands of files in a directory in less than a second.
    *   **Libraries**: `os`.

### Compression & Decompression
*   **[`compress_tif_batch.bat`](file:///C:/Users/clark/Documents/toolbox/file_utilities/compress_tif_batch.bat) & [`uncompress_tif_batch.bat`](file:///C:/Users/clark/Documents/toolbox/file_utilities/uncompress_tif_batch.bat)**:
    *   **Purpose**: Batch scripts calling command-line compression utilities (`mr_file.exe`) to compress raw orthophotos to JPEG formats or uncompress them back to TIFFs.

### Table Operations & Randomization
*   **[`join_table_and_copy_fields.py`](file:///C:/Users/clark/Documents/toolbox/file_utilities/join_table_and_copy_fields.py)**:
    *   **Purpose**: Joins database tables (e.g., `.csv` metrics) to spatial shapefiles, writes data into a new field, and cleans up the join.
    *   **Libraries**: `arcpy`.
*   **[`import_csv_trial.py`](file:///C:/Users/clark/Documents/toolbox/file_utilities/import_csv_trial.py)**:
    *   **Purpose**: Testing script for importing CSV files as raster objects.
*   **[`generate_random_number_arcgis.py`](file:///C:/Users/clark/Documents/toolbox/file_utilities/generate_random_number_arcgis.py)**:
    *   **Purpose**: Python expression block for the ArcGIS Field Calculator to write random float values between 0 and 1 to attribute tables.
    *   **Libraries**: `numpy`.

### Workload Simulation
*   **[`simulated_copy_workload.py`](file:///C:/Users/clark/Documents/toolbox/file_utilities/simulated_copy_workload.py)**:
    *   **Purpose**: Reads a file list and simulates copy workloads by printing operations and sleeping at random intervals (0-3s). Used for performance benchmarking and testing processing pipelines.
    *   **Libraries**: `csv`, `time`, `random`.
