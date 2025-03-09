Lesson for a high school geometry and geography class on Coordinate Reference Systems (CRS) and distance calculations using Python:

---

## Lesson: Coordinate Reference Systems (CRS) and Distance Calculations with Python
---

### Objectives
- Understand the concept of Coordinate Reference Systems (CRS) and their importance in geospatial data.
- Learn how to work with CRS in Python using Geopandas and other libraries.
- Perform distance calculations in different units (meters, feet) using Python.

### Introduction to CRS
Coordinate Reference Systems (CRS) are essential in geospatial data for accurately representing the Earth's surface. They define how the two-dimensional, projected map in your GIS relates to real places on Earth. The most common CRS is WGS84, which is used in GPS and global mapping.

### WGS84: The Global Standard
- **WGS84**: World Geodetic System 1984
- **Units**: Degrees for latitude and longitude
- **Ellipsoid Model**: Approximates the Earth’s shape
  - Semi-major axis: 6,378,137 meters
  - Flattening: 1/298.257223563

### Working with CRS in Python
We’ll use Geopandas to handle CRS and perform distance calculations.

#### Installing Required Libraries
```bash
pip install geopandas shapely geopy
```

#### Example: Creating and Reprojecting a GeoDataFrame
```python
import geopandas as gpd
from shapely.geometry import Point

# Create a GeoDataFrame with a Point in WGS84 (EPSG:4326)
gdf = gpd.GeoDataFrame({'geometry': [Point(-73.9851, 40.7589)]}, crs='EPSG:4326')

# Check the CRS
print(gdf.crs)

# Reproject the GeoDataFrame to UTM zone 18N (EPSG:32618)
gdf_utm = gdf.to_crs('EPSG:32618')

# Check the new CRS
print(gdf_utm.crs)
```

### Distance Calculations
There are two main types of distance calculations: geodesic (curved surface) and planar (flat surface).

#### Geodesic Distance with Geopy
```python
from geopy.distance import geodesic

# Define two points with latitude and longitude
point1 = (40.7589, -73.9851)  # New York, NY
point2 = (34.052235, -118.243683) # Los Angeles, CA

# Calculate the geodesic distance in meters
distance_meters = geodesic(point1, point2).meters
print(f'Distance in meters: {distance_meters}')

# Convert the distance to feet
distance_feet = distance_meters * 3.28084
print(f'Distance in feet: {distance_feet}')
```

#### Planar Distance with Shapely
```python
from shapely.geometry import Point

# Define two points with projected coordinates (e.g., UTM)
point1 = Point(500000, 4649776)  # Example UTM coordinates
point2 = Point(600000, 4649776)  # Example UTM coordinates

# Calculate the planar distance in meters
distance_meters = point1.distance(point2)
print(f'Distance in meters: {distance_meters}')

# Convert the distance to feet
distance_feet = distance_meters * 3.28084
print(f'Distance in feet: {distance_feet}')
```

### Conclusion
Understanding CRS and how to perform distance calculations are fundamental skills in geography and geometry. Using Python and libraries like Geopandas, Geopy, and Shapely, you can accurately measure distances and work with geospatial data.

### Additional Resources
- [Geopandas Documentation](https://geopandas.org/)
- [Shapely Documentation](https://shapely.readthedocs.io/)
- [Geopy Documentation](https://geopy.readthedocs.io/)
---