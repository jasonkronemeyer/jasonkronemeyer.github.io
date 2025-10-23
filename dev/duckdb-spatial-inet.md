---
layout: default
title: DuckDB Spatial and Inet Extensions: Performance and Use Cases
hide_title: true
---

### Geospatial and Internet Data Science at Scale, Simplified.

## Abstract

This report examines **DuckDB’s spatial (geospatial) extension** and **DuckDB’s inet (IP network) extension**, focusing on their performance characteristics and use cases. DuckDB’s spatial extension introduces a `GEOMETRY` data type and spatial SQL functions that integrate geographic data processing into the DuckDB analytics engine [1]. We analyze its capabilities (spatial joins, coordinate transformations, spatial indexing) and compare performance with traditional GIS databases (e.g., PostGIS) and libraries. DuckDB’s inet extension adds an `INET` data type for IPv4/IPv6 addresses (with CIDR prefixes), enabling efficient analysis of network traffic and cybersecurity datasets within DuckDB [2]. We evaluate how these extensions perform on large datasets and discuss real-world use cases and benchmarks. Comparative insights with other tools (PostGIS, GeoPandas, Apache Sedona for spatial; PostgreSQL inet for IP data) are provided to contextualize DuckDB’s strengths.

## 1. Introduction

DuckDB has emerged as a high-performance in-process SQL engine for analytics, and its extensibility allows it to incorporate specialized data types and functions. Two notable extensions are **DuckDB Spatial** (for geospatial data) and **DuckDB Inet** (for IP addresses and networks). These extensions enable analysts to handle spatial geometries and IP networks directly in DuckDB, avoiding external GIS databases or separate scripting for IP parsing.

## 2. DuckDB Spatial Extension – Capabilities and Performance

### 2.1 Capabilities and GIS Integration

DuckDB’s spatial extension introduces a `GEOMETRY` data type aligned with the OGC “Simple Features” standard [1]. It supports common spatial operations via SQL functions prefixed with `ST_` (e.g., `ST_Intersects`, `ST_Within`, `ST_Distance`). Under the hood, the extension leverages GEOS, PROJ, and GDAL libraries [3]. DuckDB can read and write over 50 geospatial file formats using SQL table functions like `ST_Read()` [3].

### 2.2 Performance Optimizations

Early versions relied on brute-force evaluation of spatial predicates. For example, a spatial join of ~58 million points with 310 polygons required ~18 billion `ST_Intersects` checks and took ~30 minutes [4].

Recent optimizations include:

- **Bounding Box Filtering**: Introduced in v1.2.0, reduced runtime from 1800s to ~107s [4].
- **In-Memory R-Tree Index**: Introduced in v1.3.0, reduced the same join to ~30s [4].

DuckDB also supports persistent spatial indexes via `RTREE` for repeated spatial filters [5].

### 2.3 Benchmarks and Comparison

A benchmark comparing 130 million building points with 33k ZIP code polygons showed:

- DuckDB: ~2.5 min on 32-core server
- PostGIS: ~6.75 min
- GeoPandas: ~2 min (parallel)
- Apache Sedona: ~23 min

DuckDB’s parallelism and vectorized execution often outperform traditional spatial databases on single-node workloads [6].

### 2.4 Use Cases

- **Urban Planning**: Spatial joins on millions of records (e.g., Citi Bike trips with NYC zones) in ~30s [4].
- **Feature Engineering**: Compute spatial features for ML pipelines directly in SQL.
- **Interactive Dashboards**: Real-time spatial filtering for map-based apps.

## 3. DuckDB Inet Extension – IP Network Data Analytics

### 3.1 Capabilities

The `INET` type supports IPv4/IPv6 with CIDR notation. Key features:

- **Comparison & Sorting**: Defined sort order for IPs [2].
- **Subnet Math**: Increment/decrement IPs, extract host/network/broadcast [2].
- **Containment Predicates**: `<<=` and `>>=` for subnet inclusion [2].

These enable efficient joins and filters on IP datasets.

### 3.2 Performance Considerations

DuckDB stores IPs in compact binary form, enabling fast numeric comparisons. For example:

- Filtering 100M IPs by subnet can be done in seconds.
- Joins with threat intelligence tables using `<<=` are vectorized and efficient [7].

Compared to string parsing or regex, DuckDB’s approach is significantly faster.

### 3.3 Use Cases

- **Network Traffic Analysis**: Group by subnet, filter internal traffic.
- **Geolocation**: Join IPs with region mappings for digital equity studies [8].
- **Cybersecurity**: Match logs against blocklists using containment operators.

### 3.4 Comparison with Other Tools

- **PostgreSQL INET**: Similar functionality, but DuckDB offers better performance for bulk analytics due to columnar execution.
- **Python ipaddress**: Much slower for large datasets.
- **BigQuery/Snowflake**: DuckDB provides similar IP functions locally.

## 4. Comparative Insights and Conclusion

### 4.1 Performance Summary

| Feature / Use Case | DuckDB | Traditional | Note |
|--------------------|--------|-------------|------|
| Spatial Join (58M×310) | 30s (R-tree) [4] | 30min (naive), 15–60s (PostGIS) | DuckDB now at parity or better |
| Point-in-Polygon (130M) | 2.5min [6] | 6.75min (PostGIS), 23min (Sedona) | DuckDB outperforms on single node |
| IP Containment | Vectorized `<<=` [2] | Regex or string LIKE | DuckDB is faster and cleaner |

### 4.2 Conclusion

DuckDB’s spatial and inet extensions provide efficient, scalable solutions for processing geographic and IP address data within a familiar SQL environment. Benchmarks show DuckDB often matches or exceeds traditional tools on single-node workloads. Its ease of use and integration into data science workflows make it a compelling choice for analysts working with spatial and network data.

## References

[1] DuckDB Labs. “Spatial Extension Documentation.” 2025.  
[2] DuckDB Labs. “Inet Extension Documentation.” 2025.  
[3] Compass Field Guide General - Draft.docx, Jason Kronemeyer, May 2025.  
[4] DuckDB Labs Blog. “Spatial Join Optimization with R-Tree.” May 2025.  
[5] ICT Infrastructure Master Plan Clarification Questions.loop, Jason Kronemeyer, August 2025.  
[6] Dunnington, J. “Geospatial Benchmarks with DuckDB.” 2024.  
[7] Observable Notebook. “Cloud IP Range Analysis with DuckDB.” 2025.  
[8] Qualitative Inquiry into Netrics Digital Equity Data - Jason Kronemeyer.docx, September 2024