# Reference Data Lists

This folder contains CSV and tabular files that act as inputs or logs for the batch processing scripts within this repository.

## 📄 Files

*   **[`Full_List.csv`](file:///C:/Users/clark/Documents/toolbox/data/Full_List.csv)**:
    *   **Description**: A list of orthomosaic image filenames (`.tif`) used as the indexing inventory for various batch copy/paste routines.
*   **[`list.csv`](file:///C:/Users/clark/Documents/toolbox/data/list.csv)**:
    *   **Description**: A standard target copy list containing a subset of image filenames (e.g. `1708_82.tif`) representing subset research flight paths.
*   **[`rmapList.csv`](file:///C:/Users/clark/Documents/toolbox/data/rmapList.csv)**:
    *   **Description**: List containing full absolute file system paths of input `.tif` files. Used by the sequential `domain_buffer_clip` scripts to run batch spatial analysis.
*   **[`rmapList_batchclip.csv`](file:///C:/Users/clark/Documents/toolbox/data/rmapList_batchclip.csv)**:
    *   **Description**: High-volume log table of batch clipping commands and spatial extents. Used by ERDAS IMAGINE Modeler commands.
