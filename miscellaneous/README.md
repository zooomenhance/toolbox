# Miscellaneous Scripts

This folder contains standalone scripts that are outside of the primary forestry, remote sensing, and GIS geoprocessing categories.

## 📄 Scripts

*   **[`collatz.py`](file:///C:/Users/clark/Documents/toolbox/miscellaneous/collatz.py)**:
    *   **Purpose**: Simulates the Collatz Conjecture (the 3n+1 problem). Prompts for a starting integer and prints the sequence path until it reaches 1.
*   **[`ascii_art.py`](file:///C:/Users/clark/Documents/toolbox/miscellaneous/ascii_art.py)**:
    *   **Purpose**: Resizes an input image, converts it to grayscale, and maps pixel values to standard ASCII characters to output custom text-based ASCII art.
    *   **Libraries**: `PIL` (Pillow).
*   **[`time_test.py`](file:///C:/Users/clark/Documents/toolbox/miscellaneous/time_test.py)**:
    *   **Purpose**: A simple benchmark template to measure script execution timing.
    *   **Libraries**: `time`, `arcpy`.
*   **[`us_place_names_analysis.py`](file:///C:/Users/clark/Documents/toolbox/miscellaneous/us_place_names_analysis.py)**:
    *   **Purpose**: Parses USGS national place name database files (`.dbf`), converts the data to Pandas DataFrames, and calculates frequency stats to find the most common names in the US.
    *   **Libraries**: `pandas`, `dbfread` / `simpledbf`.
