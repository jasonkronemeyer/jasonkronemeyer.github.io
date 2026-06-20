---
layout: post
title: "Accessing O’Sullivan Lake Bathymetry Through Ontario GeoHub"
date: 2026-06-20
categories: [maps, GIS, research]
tags: [bathymetry, Ontario, GeoHub, LiDAR, GPX, GeoJSON, MBTiles]
status: research
excerpt: "A research note on finding the historic O’Sullivan Lake bathymetry map through Ontario GeoHub and outlining a modern GPS-ready update workflow."
description: "How to access the historic O’Sullivan Lake bathymetry map near Dunn’s Outpost and a practical workflow for modernizing it with current shoreline data and LiDAR."
---

## The map exists, but it lives inside the viewer

For the O’Sullivan Lake associated with Dunn’s Outpost, the official Ontario bathymetry map is available through the Ontario GeoHub **Historic Bathymetry Maps** viewer rather than as a stable standalone file URL.

**Direct viewer link:**  
[Ontario GeoHub Historic Bathymetry Maps — centered on O’Sullivan Lake](https://geohub.lio.gov.on.ca/maps/mnrf::historic-bathymetry-maps/explore?location=50.066,-86.807,11)

Ontario’s own viewer instructions note that lake map downloads appear only after selecting a lake polygon in the map.

### How to reach the download

1. Open the GeoHub viewer.  
2. Zoom in slightly if needed.  
3. Click the O’Sullivan Lake polygon.  
4. Use the pop-up links to open the scanned bathymetry map PDF or TIFF when available.  

This historic collection is still valuable because many northern lakes continue to rely on these scanned survey products as their primary public bathymetry reference.

## A modernized overlay workflow

If I were building a usable field-ready version of this map, I would treat it as a three-layer modernization workflow rather than a direct redraw.

### Layer A — Digitized historic contours

- Extract contour lines from the scanned PDF or TIFF  
- Convert them to vector features  
- Normalize interval labeling and clean geometry  
- Align them to a current basemap in EPSG:4326 or EPSG:3857  

Potential outputs:

- GPX for GPS units  
- KML for Google Earth  
- GeoJSON for GIS workflows  
- MBTiles for offline shaded map use  

### Layer B — Shoreline correction

Historic Ministry maps often reflect older shoreline conditions. A modern workflow should:

- Replace the historic shoreline with current hydrography  
- Correct visible georeferencing drift  
- Adjust for water-level change where evidence supports it  

### Layer C — Depth shading

Once contours are cleaned and aligned, they can support:

- Bathymetric tinting  
- Hillshade-style underwater relief  
- Offline raster exports for mobile mapping apps  

## A LiDAR-based depth update plan

The historic map is authoritative as a source document, but it may no longer describe current conditions perfectly. A better update path is to use the historic contours as calibration data inside a newer terrain workflow.

### Step 1 — Acquire elevation data

- Use Ontario open LiDAR where coverage exists  
- Fall back to Copernicus or other public DEM sources where LiDAR is unavailable  

### Step 2 — Estimate basin form

- Remove the lake surface from the terrain model  
- Interpolate submerged form from surrounding slopes and known contour structure  
- Apply hydrologic constraints so the basin remains realistic  

### Step 3 — Calibrate against the historic map

- Anchor the model to known contour depths from the scanned survey  
- Reconcile mismatches between shoreline position and historic linework  
- Carry uncertainty forward rather than presenting the update as exact  

### Step 4 — Export updated products

- 1 m, 2 m, or 5 m contour sets  
- Shaded bathymetric raster layers  
- Optional 3D basin visualization for analysis  

## Why this matters

The GeoHub scan is the starting point, not the finished product. For navigation, habitat analysis, or field use, the most useful approach is to preserve the historic survey while translating it into modern vector, raster, and GPS-friendly formats.

## Notes

- Viewer access: Ontario GeoHub Historic Bathymetry Maps  
- Lake-specific downloads depend on clicking the lake polygon in the viewer  
- Any LiDAR-derived update should be treated as an estimate unless supported by new in-water sounding data  
