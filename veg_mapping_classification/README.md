# Vegetation Mapping and Classification

This directory contains advanced statistical workflows and geoprocessing scripts used for mapping forest structures, canopy height, canopy cover classification, and species modeling.

## 📄 Scripts

### Canopy Height & Cover Classification
*   **[`veg_class_assignment_carson_v1.py`](file:///C:/Users/clark/Documents/toolbox/veg_mapping_classification/veg_class_assignment_carson_v1.py) & [`veg_class_assignment_carson_v2.py`](file:///C:/Users/clark/Documents/toolbox/veg_mapping_classification/veg_class_assignment_carson_v2.py)**:
    *   **Purpose**: Processes forest metrics for the Carson National Forest. Uses an `UpdateCursor` to assign canopy size classes based on heights and data sources.
    *   **Libraries**: `arcpy`.
*   **[`veg_class_assignment_santafe_v1.py`](file:///C:/Users/clark/Documents/toolbox/veg_mapping_classification/veg_class_assignment_santafe_v1.py) to [`veg_class_assignment_santafe_v3_cleaned.py`](file:///C:/Users/clark/Documents/toolbox/veg_mapping_classification/veg_class_assignment_santafe_v3_cleaned.py)**:
    *   **Purpose**: Performs canopy size and height class assignment for Santa Fe National Forest vector segments.
    *   **Libraries**: `arcpy`.
*   **[`attribute_table_creation_carson.py`](file:///C:/Users/clark/Documents/toolbox/veg_mapping_classification/attribute_table_creation_carson.py)**:
    *   **Purpose**: Automatically populates forestry database attributes (Lifeform, Canopy Cover, Size Class) for Carson National Forest vectors.
    *   **Libraries**: `arcpy`.
*   **[`compute_canopy_strata_cover.py`](file:///C:/Users/clark/Documents/toolbox/veg_mapping_classification/compute_canopy_strata_cover.py)**:
    *   **Purpose**: Computes forestry canopy cover percentage stats dynamically using height strata count layers.
    *   **Libraries**: `arcpy`, `os`.

### Machine Learning & Zonal Statistics
*   **[`zonal_stats_rf_classifier.py`](file:///C:/Users/clark/Documents/toolbox/veg_mapping_classification/zonal_stats_rf_classifier.py)**:
    *   **Purpose**: Runs spatial zonal statistics on image segments and prepares inputs for Random Forest classifications using Pandas, Geopandas, and Numpy.
    *   **Libraries**: `arcpy`, `pandas`, `geopandas`, `numpy`, `time`.
*   **[`vegetation_mapping_random_forest.R`](file:///C:/Users/clark/Documents/toolbox/veg_mapping_classification/vegetation_mapping_random_forest.R)**:
    *   **Purpose**: Random Forest predictive model implementation in R. Trains on sample plots and applies the predictive classification tree to map forest types.
    *   **Libraries**: `randomForest`.
*   **[`cibola_merge_forestry_data.R`](file:///C:/Users/clark/Documents/toolbox/veg_mapping_classification/cibola_merge_forestry_data.R) & [`cibola_merge_phodar_data.R`](file:///C:/Users/clark/Documents/toolbox/veg_mapping_classification/cibola_merge_phodar_data.R)**:
    *   **Purpose**: R scripts that read, align column structures of, and join multiple Landsat, NAIP, and DEM zonal statistics tables for the Cibola National Forest and Grasslands.
    *   **Libraries**: `data.table`.
*   **[`coronado_merge_forestry_data.R`](file:///C:/Users/clark/Documents/toolbox/veg_mapping_classification/coronado_merge_forestry_data.R)**:
    *   **Purpose**: Similar dataset merging script designed for Coronado National Forest plot data.
    *   **Libraries**: `data.table`.

### Separability Analysis
*   **[`uwc_separability_analysis.R`](file:///C:/Users/clark/Documents/toolbox/veg_mapping_classification/uwc_separability_analysis.R)**:
    *   **Purpose**: Performs spectral separability analysis of vegetation classes for the Uinta-Wasatch-Cache National Forest. Computes Mahalanobis, Bhattacharyya, and Jeffries-Matusita distances between multivariate distributions.
    *   **Libraries**: `ggplot2`, `geomnet`, `plyr`, `ape`.
