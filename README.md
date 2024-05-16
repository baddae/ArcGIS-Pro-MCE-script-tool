# ArcGIS-Pro-MCE-script-tool
Multi-Criteria Evaluation Script Tool for ArcGIS Pro

# Multi-Criteria Evaluation Script Tool

This repository contains a Python script tool for performing multi-criteria evaluation (MCE) using ArcGIS Pro. The tool allows users to input multiple raster layers and assign a weight of importance to each layer. The weights are used to scale the raster values, and the scaled rasters are then summed to produce a final output raster.

## Description

The multi-criteria evaluation script tool is designed to facilitate spatial analysis by combining multiple raster datasets, each representing a different criterion. The tool applies user-defined weights to each raster and computes a weighted sum to produce an output raster that reflects the combined importance of the input criteria.

## Features

- Accepts multiple raster layers as input.
- Allows user to assign a weight of importance to each raster.
- Ensures that the weights sum up to 1.
- Multiplies each raster cell value by the corresponding weight.
- Sums the weighted rasters to create a final output raster.

## Usage



