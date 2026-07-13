# GIS Vector Operations

This directory contains scripts for processing, converting, and analyzing vector dataset geometries (points, polylines, and polygons) across ArcGIS, QGIS, and custom files.

## 📄 Scripts

### GPS Tracking & GPX Import
*   **[`gpx_to_shapefile.py`](file:///C:/Users/clark/Documents/toolbox/gis_vector/gpx_to_shapefile.py)**:
    *   **Purpose**: Batch imports GPS track files (`.gpx`) from a directory and converts them into ArcGIS spatial feature classes or shapefiles.
    *   **Libraries**: `arcpy`, `glob`, `os`.
*   **[`points_to_line.py`](file:///C:/Users/clark/Documents/toolbox/gis_vector/points_to_line.py)**:
    *   **Purpose**: Converts sequential vector point markers to linear polylines.
    *   **Libraries**: `arcpy`, `glob`, `os`.

### QGIS Console Scripts
*   **[`qgis_geojson_to_shapefile_v1.py`](file:///C:/Users/clark/Documents/toolbox/gis_vector/qgis_geojson_to_shapefile_v1.py) & [`qgis_geojson_to_shapefile_v2_batch.py`](file:///C:/Users/clark/Documents/toolbox/gis_vector/qgis_geojson_to_shapefile_v2_batch.py)**:
    *   **Purpose**: Python scripts designed to be executed directly inside the QGIS Python Console. They iterate through active or visible GeoJSON layer datasets in the map canvas and export them as ESRI Shapefiles.
    *   **Classes**: `QgsVectorFileWriter`, `iface.mapCanvas()`.

### Indexing & Mapping
*   **[`flightlines_expnum_test_v1.py`](file:///C:/Users/clark/Documents/toolbox/gis_vector/flightlines_expnum_test_v1.py) & [`flightlines_expnum_test_v2.py`](file:///C:/Users/clark/Documents/toolbox/gis_vector/flightlines_expnum_test_v2.py)**:
    *   **Purpose**: Selects flight exposures based on attribute indexes (`EXPNUM`) and projects vector path lines.
    *   **Libraries**: `arcpy`.
*   **[`big_year_map_creation.py`](file:///C:/Users/clark/Documents/toolbox/gis_vector/big_year_map_creation.py)**:
    *   **Purpose**: Processes bird-watching location coordinate CSV files, creates point layers (`MakeXYEventLayer`), generates minimum bounding envelopes/rectangles (`MinimumBoundingGeometry` with ENVELOPE parameter), and maps paths.
    *   **Libraries**: `arcpy`, `glob`, `shutil`.
