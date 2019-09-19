# Automated Map of Australia

* A Python script that utilizes the arcpy site package. 

* This program works in ArcMap to run through a series of basic data entry and geoprocessing tasks to create a map of Australia. 

* It displays the country's boundary, major rivers, and labeled cities without having to do so manually.



## What does the program do exactly?

1) Sets up a workspace, designates the respective geodatabase, and enters MapDocument properties.

2) Adds a layer for the country boundary, world cities, and world rivers from the geodatabase to the data frame and defines an appropriate coordinate system for them.

3) Performs the "clip" geoprocessing tool on the cities and rivers layer to the country boundary.

4) Removes the original cities and rivers layers from the table of contents.

5) Labels the cities by name.

6) Prompts the user to save the .mxd file.



## Running the program

* This script runs in the ArcMap Python window. ArcMap is required.

* Additionally, a geodatabase must be set up preemptively for the script to pull the necessary files.

