# ArcGIS-Pro-MCE-script-tool
Multi-Criteria Evaluation Script Tool for ArcGIS Pro

# Multi-Criteria Evaluation Script Tool

This repository contains a Python script tool for performing multi-criteria evaluation (MCE) using ArcGIS Pro. The tool allows users to input multiple raster layers and assign a weight of importance to each layer. The weights are used to scale the raster values, and the scaled rasters are then summed to produce a final output raster. This tool can be utilized for conducting site suitability assessments crucial for decisions on optimal locations for facilities such as waste plants, wind farms, and solar panels.

## Description

The multi-criteria evaluation script tool is designed to facilitate spatial analysis by combining multiple raster datasets, each representing a different criterion. The tool applies user-defined weights to each raster and computes a weighted sum to produce an output raster that reflects the combined importance of the input criteria.

## Example
Suppose you have three raster layers representing different criteria for urban planning (e.g., proximity to roads, slope, and land use). You can use this tool to combine these criteria by assigning weights based on their importance (e.g., 0.4 for proximity to roads, 0.3 for slope, and 0.3 for land use). The tool will compute the weighted sum of these rasters and produce a final output raster that can be used for decision making.

Imagine you are evaluating potential sites for a wind farm. You have several raster layers representing different criteria such as wind speed, proximity to transmission lines, land use, and environmental constraints. Using this tool, you can assign weights to these criteria based on their significance (e.g., 0.5 for wind speed, 0.2 for proximity to transmission lines, 0.2 for land use, and 0.1 for environmental constraints). The tool will then calculate the weighted sum of these layers, resulting in a final output raster that highlights the most suitable locations for a wind farm.

## Features

- Accepts multiple raster layers as input.
- Allows user to assign a weight of importance to each raster.
- Ensures that the weights sum up to 1.
- Multiplies each raster cell value by the corresponding weight.
- Sums the weighted rasters to create a final output raster.

## Usage

Define the Script Tool Parameters:

- Parameter 1: Raster Layers
Label: Raster Layers
Name: raster_layers
Data Type: Raster Layer
Type: Multivalue
Direction: Input
- Parameter 2: Weights
Label: Weights
Name: weights
Data Type: Double
Type: Multivalue
Direction: Input
- Parameter 3: Output Raster
Label: Output Raster
Name: output_raster
Data Type: Raster Dataset
Type: Derived Output
Direction: Output



