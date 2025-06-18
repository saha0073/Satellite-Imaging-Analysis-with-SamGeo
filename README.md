# sam-geospatial

This repository demonstrates the use of the [Segment Anything Model for Geospatial Data (samgeo)](https://samgeo.gishub.org/) to automatically generate object masks and annotations from satellite imagery.

## What is samgeo?

[samgeo](https://samgeo.gishub.org/) is a Python package that adapts the powerful Segment Anything Model (SAM) for geospatial data analysis. While SAM was originally designed for general image segmentation, samgeo extends its capabilities to work seamlessly with geospatial raster data such as satellite and aerial imagery. It provides tools to segment objects, generate masks, and export results in both raster and vector formats, making it easy to integrate deep learning segmentation into geospatial workflows with minimal code.

## Installation

You only need to install the following packages to get started:

```bash
pip install segment-geospatial
conda install -c conda-forge gdal
```

This will install samgeo and all its dependencies. Make sure GDAL is installed via conda for best compatibility with geospatial data.

## Overview

The notebook in this repository follows the official [samgeo automatic mask generator example](https://samgeo.gishub.org/examples/automatic_mask_generator/). It shows how to:

- Download or use your own satellite image (GeoTIFF)
- Visualize the image on an interactive map using [leafmap](https://leafmap.org/)
- Use the Segment Anything Model (SAM) via the `samgeo` Python package to automatically segment objects in the image
- Save the generated masks as a GeoTIFF file (`masks.tif`)
- Visualize the masks and object annotations
- Export the annotations to vector formats (GeoPackage, Shapefile, or GeoJSON)

## Sample Results

**Satellite Image**  
![Satellite](satellite.png)

**Generated Mask**  
![Mask](masks.png)

**Annotations**  
![Annotations](annotations.png)

## Workflow

1. **Install dependencies**: Install `segment-geospatial` and `gdal` as described above.
2. **Load and display satellite imagery**: Use `leafmap` to display the satellite image and select a region of interest.
3. **Automatic mask generation**: Use `SamGeo.generate()` to segment the image and save the results as a mask GeoTIFF.
4. **Visualize results**: Display the generated masks and annotations using `samgeo` and `leafmap`.
5. **Export annotations**: Convert the mask raster to vector data for further analysis or GIS applications.

## Example Usage

```python
from samgeo import SamGeo
import leafmap

# Initialize map and display satellite image
m = leafmap.Map(center=[LAT, LON], zoom=17)
m.add_basemap("SATELLITE")
m

# Initialize SAM and generate masks
sam = SamGeo(model_type="vit_h")
sam.generate("satellite.tif", output="masks.tif", foreground=True, unique=True)

# Visualize masks
sam.show_masks(cmap="binary_r")

# Export annotations
sam.show_anns(axis="off", alpha=1, output="annotations.tif")
sam.tiff_to_vector("masks.tif", "masks.gpkg")
```

## Reference
- Official example: [samgeo automatic mask generator](https://samgeo.gishub.org/examples/automatic_mask_generator/)
- [Segment Anything Model for Geospatial Data (samgeo)](https://samgeo.gishub.org/)
- [leafmap](https://leafmap.org/)

---

