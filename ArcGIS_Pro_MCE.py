"""
Multi-Criteria Evaluation Script Tool
=====================================

This script tool performs multi-criteria evaluation (MCE) in ArcGIS Pro. The tool allows users
to input multiple raster layers, assign a weight of importance to each layer, and compute a 
weighted sum to produce a final output raster. The weights must sum up to 1.

Usage:
- Add this script as a script tool in ArcGIS Pro.
- Input multiple raster layers and their corresponding weights.
- The script will multiply each raster cell value by the corresponding weight and sum the results.

Author: Bright Addae
License: MIT License

Copyright (c) 2024 Bright Addae
"""

import arcpy
from arcpy.sa import *

# Ensure the Spatial Analyst extension is available
arcpy.CheckOutExtension("Spatial")

def main():
    # Input parameters
    raster_inputs = arcpy.GetParameterAsText(0).split(";")  # List of input raster layers
    weights = arcpy.GetParameterAsText(1).split(";")        # Corresponding weights for each raster
    output_raster = arcpy.GetParameterAsText(2)             # Output raster path

    # Convert weights to float and check if they add up to 1
    weights = [float(weight) for weight in weights]
    if sum(weights) != 1.0:
        arcpy.AddError("The weights of importance must add up to 1.")
        raise ValueError("The weights of importance must add up to 1.")
    
    # Initialize the final weighted raster to None
    final_raster = None

    # Iterate over raster inputs and their corresponding weights
    for raster_path, weight in zip(raster_inputs, weights):
        # Load the raster
        raster = Raster(raster_path)
        
        # Multiply the raster by its weight
        weighted_raster = raster * weight
        
        # Add to the final raster
        if final_raster is None:
            final_raster = weighted_raster
        else:
            final_raster += weighted_raster

    # Save the final raster
    final_raster.save(output_raster)
    arcpy.AddMessage(f"Multi-criteria evaluation completed. Output saved to {output_raster}")

if __name__ == "__main__":
    main()

