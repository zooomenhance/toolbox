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

### Machine Learning & Zonal Statistics
*   **[`zonal_stats_rf_classifier.py`](file:///C:/Users/clark/Documents/toolbox/veg_mapping_classification/zonal_stats_rf_classifier.py)**:
    *   **Purpose**: Runs spatial zonal statistics on image segments and prepares inputs for Random Forest classifications using Pandas, Geopandas, and Numpy.
    *   **Libraries**: `arcpy`, `pandas`, `geopandas`, `numpy`, `time`.
*   **[`vegetation_mapping_random_forest.R`](file:///C:/Users/clark/Documents/toolbox/veg_mapping_classification/vegetation_mapping_random_forest.R)**:
    *   **Purpose**: Random Forest predictive model implementation in R. Trains on sample plots and applies the predictive classification tree to map forest types.
    *   **Libraries**: `randomForest`.

### Separability Analysis
*   **[`uwc_separability_analysis.R`](file:///C:/Users/clark/Documents/toolbox/veg_mapping_classification/uwc_separability_analysis.R)**:
    *   **Purpose**: Performs spectral separability analysis of vegetation classes for the Uinta-Wasatch-Cache National Forest. Computes Mahalanobis, Bhattacharyya, and Jeffries-Matusita distances between multivariate distributions.
    *   **Libraries**: `ggplot2`, `geomnet`, `plyr`, `ape`.
