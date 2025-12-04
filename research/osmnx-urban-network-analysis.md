---
layout: page
title: "OSMnx Urban Network Analysis for Digital Equity"
permalink: /research/osmnx-urban-network-analysis/
---

# OSMnx Urban Network Analysis for Digital Equity

{:.lead}
Integrating street network topology and urban morphology analysis with broadband infrastructure planning and digital equity research.

**Research Type**: Planning Document  
**Status**: Research Plan • 2025  
**Research Area**: Spatial Data for Community Development

{% include callout.html type="info" title="Planning Status" content="This document outlines future research directions integrating OSMnx (OpenStreetMap NetworkX) capabilities with existing digital equity and broadband infrastructure analysis. Projects described are in the planning and design phase." %}

---

## Introduction

**OSMnx** is a Python package that downloads street networks, buildings, bike lanes, rail, and walkable paths from OpenStreetMap and converts them into clean, routable NetworkX graphs. It provides powerful capabilities for:
- **Urban network analysis** and street network topology studies
- **Accessibility modeling** through drive-time isochrones and routing optimization
- **Integration with spatial tools** like GeoPandas, Matplotlib, and graph databases
- **Multi-modal transportation** analysis (pedestrian, bicycle, vehicle networks)

### Relevance to Digital Equity Research

Digital accessibility is fundamentally tied to physical accessibility. Communities isolated by sparse road networks, long travel distances, or limited transportation options face compounded barriers to digital inclusion. Understanding the relationship between **physical network topology** and **digital infrastructure deployment** enables more effective and equitable broadband planning.

### Connection to Existing Repository Work

This research builds directly on established work in this repository:
- **Maps directory**: BEAD funding visualization, EUP connectivity analysis, RDOF coverage mapping
- **Spatial analytics**: PostGIS, Apache Sedona, Neo4j for geospatial data processing
- **Digital equity focus**: [Digital Navigation & Maslow's Hierarchy](/research/digital-navigation-maslow/) framework
- **Regional initiatives**: EUPConnect Collaborative and Michigan broadband deployment

By integrating OSMnx network analysis with existing broadband infrastructure data, we can develop more nuanced understanding of **access patterns**, **deployment constraints**, and **equity implications** in rural and underserved communities.

---

## Research Project Ideas

### 🗺️ **Project 1: Digital Access Accessibility Study**

#### Overview
Use OSMnx to calculate drive-time and walk-time isochrones from public WiFi locations, libraries, and community centers in Michigan's Eastern Upper Peninsula (EUP), identifying populations beyond reasonable travel distance to digital access points.

#### Research Questions
- What percentage of EUP residents live more than 15/30/45 minutes from public internet access?
- How does road network topology affect accessibility to digital resources in rural areas?
- Which communities have the greatest physical barriers to digital inclusion resources?

#### Methodology
1. **Network extraction**: Download EUP road networks using OSMnx
2. **Access point mapping**: Geocode libraries, community centers, schools with public WiFi
3. **Isochrone generation**: Calculate multi-modal travel time polygons (drive, walk, bike)
4. **Population analysis**: Overlay with Census block data to quantify affected populations
5. **Broadband integration**: Combine with BEAD/RDOF coverage data for comprehensive view

#### Deliverables
- **Interactive accessibility maps** showing travel time zones
- **Accessibility scores** by census tract and community
- **Policy recommendations** for strategic placement of digital access points
- **Vulnerability analysis** identifying most isolated communities

#### Technical Stack
- OSMnx for network analysis and routing
- GeoPandas for spatial data manipulation
- Folium for interactive web mapping
- DuckDB for efficient spatial queries
- Integration with existing BEAD/RDOF GeoJSON datasets

---

### 🛣️ **Project 2: Infrastructure Routing Optimization**

#### Overview
Model optimal fiber deployment paths using road network topology, analyzing existing infrastructure corridors (roads, utilities) for broadband buildout cost-distance analysis.

#### Research Questions
- What are the most cost-effective routes for connecting unserved locations?
- How can existing road network analysis inform middle-mile and last-mile deployment?
- Which communities offer natural "hub" locations for network expansion?

#### Methodology
1. **Network analysis**: Extract road networks with attributes (width, surface type, traffic)
2. **Corridor identification**: Map existing utility easements and rights-of-way
3. **Cost modeling**: Assign deployment costs based on terrain, distance, infrastructure access
4. **Optimization algorithms**: Use NetworkX shortest path and minimum spanning tree algorithms
5. **Scenario planning**: Model multiple deployment strategies and compare outcomes

#### Deliverables
- **Optimized route maps** for fiber deployment
- **Cost estimates** for connecting priority unserved locations
- **Prioritization framework** based on cost per household and equity factors
- **Network topology recommendations** for resilience and redundancy

#### Integration with Existing Work
- Leverage BEAD awarded ISP data from `maps/BEAD_EUP_interactive_awarded_ISP_map.html`
- Incorporate RDOF coverage zones from `merc_rdof_default_oct_2024.html`
- Integrate with GeoJSON datasets for precise location targeting

---

### 📊 **Project 3: Digital Equity Composite Scoring**

#### Overview
Create a multi-factor digital equity index combining broadband availability with network accessibility metrics, walkability/drivability scores, and proximity to digital literacy resources.

#### Research Questions
- How do physical connectivity and digital connectivity interact to affect equity?
- What composite metrics best capture multi-dimensional digital inclusion?
- Which communities face compounded disadvantages across multiple factors?

#### Methodology
1. **Factor development**:
   - **Broadband availability**: Speed, provider competition, affordability (from FCC data)
   - **Network accessibility**: Road network connectivity, centrality measures
   - **Physical access**: Distance to digital resources, public transportation availability
   - **Walkability scores**: Pedestrian network analysis, sidewalk connectivity
   - **Demographics**: ACS data on income, education, age, disability status

2. **Index construction**:
   - Normalize individual metrics to 0-100 scales
   - Apply weights based on research priorities and community input
   - Calculate composite scores by census tract and block group

3. **Validation**:
   - Compare with existing digital divide research
   - Community feedback on score relevance and accuracy
   - Statistical validation of factor relationships

#### Deliverables
- **Multi-factor equity index** with transparent methodology
- **Community scorecards** with breakdown of contributing factors
- **Comparison dashboards** showing regional and state-level benchmarking
- **Priority targeting tool** for intervention programs

#### Policy Applications
- Guide BEAD subgrant allocation decisions
- Inform Digital Navigator program placement
- Support community planning and resource allocation

---

### 🌲 **Project 4: Rural Isolation Network Metrics**

#### Overview
Quantify how road network topology affects digital inclusion by analyzing network centrality, connectivity, and resilience in sparse rural areas, comparing EUP characteristics to state and national benchmarks.

#### Research Questions
- How does network topology differ between rural and urban areas?
- What network characteristics correlate with digital infrastructure deployment patterns?
- How resilient are rural networks to disruption (road closures, disasters)?

#### Methodology
1. **Graph theory metrics**:
   - **Betweenness centrality**: Identify critical network nodes and bottlenecks
   - **Closeness centrality**: Measure average distance to all other locations
   - **Clustering coefficient**: Analyze local connectivity density
   - **Network diameter**: Calculate maximum shortest path lengths

2. **Comparative analysis**:
   - Extract networks for EUP communities and comparable regions
   - Calculate metrics for different geographic scales (township, county, region)
   - Compare to urban and suburban network characteristics
   - Benchmark against state and national averages

3. **Resilience assessment**:
   - Simulate network disruptions and measure impact
   - Identify single points of failure
   - Analyze redundancy and alternative routing options

#### Deliverables
- **Network analysis reports** with detailed metrics and visualizations
- **Vulnerability assessments** identifying at-risk communities
- **Resilience recommendations** for infrastructure planning
- **Academic paper** on rural network topology and digital equity implications

#### Research Contribution
This project advances theoretical understanding of the relationship between physical and digital connectivity, providing empirical evidence for policy discussions about rural infrastructure investment priorities.

---

## Technical Implementation

### Required Python Packages

```python
# Core spatial and network analysis
osmnx>=1.9.0          # Urban network analysis
networkx>=3.2         # Graph algorithms and analysis
geopandas>=0.14.0     # Spatial data manipulation
shapely>=2.0.0        # Geometric operations

# Visualization
folium>=0.15.0        # Interactive web maps
matplotlib>=3.8.0     # Static plotting
contextily>=1.5.0     # Basemap tiles

# Data processing
pandas>=2.1.0         # Tabular data
numpy>=1.26.0         # Numerical operations

# Integration with existing stack
duckdb>=0.10.0        # Fast spatial queries
pyarrow>=14.0.0       # Apache Arrow integration
```

### Data Sources

#### Primary Data
- **OpenStreetMap**: Street networks via OSMnx API
- **FCC Broadband Data**: National Broadband Map (BDC) data
- **Census Bureau**: ACS demographic data, TIGER/Line boundary files
- **Existing maps/**: BEAD, RDOF, EUP connectivity GeoJSON datasets

#### Supplementary Data
- **Community resources**: Library locations, community centers, WiFi hotspots
- **Infrastructure**: Utility corridors, fiber deployment maps
- **Transportation**: GTFS transit data where available
- **Elevation**: USGS DEM data for terrain analysis

### Integration with Existing Technical Stack

#### DuckDB Integration
```python
# Efficient spatial queries on large datasets
import duckdb

con = duckdb.connect()
con.execute("INSTALL spatial; LOAD spatial;")

# Join OSMnx network data with BEAD coverage
query = """
SELECT n.*, b.provider, b.max_speed
FROM network_nodes n
JOIN bead_coverage b
ON ST_Contains(b.geometry, ST_Point(n.x, n.y))
"""
```

#### Apache Sedona Integration
- Process large-scale network analysis with distributed computing
- Integrate with existing Sedona spatial analytics workflows
- Scale analysis across entire state or multi-state regions

#### Neo4j Graph Database
- Store network topology in native graph format
- Perform advanced graph algorithms (community detection, pathfinding)
- Combine road networks with social networks for comprehensive analysis

### Suggested Directory Structure

```
research/osmnx-projects/
├── notebooks/
│   ├── 01-network-extraction.ipynb
│   ├── 02-accessibility-analysis.ipynb
│   ├── 03-routing-optimization.ipynb
│   └── 04-equity-index.ipynb
├── data/
│   ├── raw/              # Downloaded OSM data
│   ├── processed/        # Cleaned networks
│   └── outputs/          # Analysis results
├── scripts/
│   ├── extract_networks.py
│   ├── calculate_isochrones.py
│   └── generate_metrics.py
├── visualizations/
│   ├── maps/             # Static map outputs
│   └── interactive/      # Folium HTML maps
└── docs/
    ├── methodology.md
    └── findings.md
```

---

## Phased Development Roadmap

### 🔧 **Phase 1: Environment Setup & Exploration**
**Timeline**: 2-3 weeks  
**Objectives**:
- Set up Python environment with OSMnx and dependencies
- Extract sample EUP street networks for pilot communities
- Develop basic network analysis workflows
- Document setup process and initial findings

**Key Milestones**:
- ✓ Install and configure OSMnx environment
- ✓ Download road networks for 3 pilot EUP communities
- ✓ Generate basic network statistics and visualizations
- ✓ Create template notebooks for future analysis

---

### 🎯 **Phase 2: Accessibility Analysis Pilot**
**Timeline**: 4-6 weeks  
**Objectives**:
- Focus on one pilot community (e.g., Sault Ste. Marie or Newberry)
- Calculate drive-time isochrones from digital access points
- Analyze population coverage and identify gaps
- Refine methodology based on pilot results

**Key Milestones**:
- ✓ Geocode all public WiFi locations and libraries in pilot area
- ✓ Generate multi-modal accessibility isochrones
- ✓ Overlay with Census population data
- ✓ Produce pilot accessibility report and maps

---

### 🌐 **Phase 3: Integration with Broadband Maps**
**Timeline**: 6-8 weeks  
**Objectives**:
- Integrate OSMnx analysis with existing BEAD/RDOF data
- Develop composite accessibility-availability metrics
- Create interactive visualization combining multiple data layers
- Expand to additional EUP communities

**Key Milestones**:
- ✓ Import and process GeoJSON broadband coverage data
- ✓ Develop spatial join workflows for network-broadband integration
- ✓ Build interactive Folium maps with layered data
- ✓ Generate community-level scorecards

---

### 📈 **Phase 4: Full Regional Analysis**
**Timeline**: 8-12 weeks  
**Objectives**:
- Scale analysis across entire EUP region
- Complete all four research projects
- Perform comparative analysis and benchmarking
- Generate comprehensive research outputs

**Key Milestones**:
- ✓ Regional network extraction and analysis
- ✓ Infrastructure routing optimization models
- ✓ Composite equity index calculation
- ✓ Network resilience assessment
- ✓ Statistical validation and testing

---

### 📝 **Phase 5: Documentation & Publication**
**Timeline**: 4-6 weeks  
**Objectives**:
- Write research papers and technical reports
- Create blog posts explaining methodology and findings
- Publish open datasets and reproducible code
- Present findings to stakeholders and communities

**Key Milestones**:
- ✓ Complete technical documentation
- ✓ Write 2-3 blog posts for general audience
- ✓ Publish datasets to GitHub/Zenodo
- ✓ Submit academic paper for peer review
- ✓ Present to EUPConnect Collaborative

---

## Connection to Existing Work

### Integration with Maps Directory

This research will enhance and extend existing map visualizations:

- **BEAD Interactive Map** (`BEAD_EUP_interactive_awarded_ISP_map.html`): Add network accessibility layers showing drive-time to awarded service areas
- **RDOF Coverage Map** (`merc_rdof_default_oct_2024.html`): Overlay optimal routing for connecting RDOF-funded locations
- **EUP Connectivity** (`eup_bead.html`): Integrate accessibility metrics with coverage data for comprehensive equity view

### Related Research

#### [Digital Navigation & Maslow's Hierarchy](/research/digital-navigation-maslow/)
- OSMnx analysis informs physical accessibility dimension of digital navigation needs
- Network metrics can help identify communities requiring intensive Digital Navigator support
- Accessibility barriers correlate with lower levels of Maslow's hierarchy (physiological and safety needs)

#### [Domain-Specific Performance](/research/domain-specific-performance/)
- Apply DuckDB spatial extension for efficient OSMnx data processing
- Benchmark OSMnx vs. alternative spatial analysis tools
- Integrate with DuckLake for managing large-scale network datasets

#### [Finding the Digital Divide](/notes/finding_digital_divide.html)
- Network accessibility provides new dimension for spatial digital divide analysis
- Combined physical-digital connectivity metrics offer holistic equity assessment

### Alignment with EUPConnect Collaborative Goals

The EUPConnect Collaborative focuses on expanding broadband access and digital equity across Michigan's Eastern Upper Peninsula. This research directly supports those goals by:

1. **Evidence-based planning**: Quantify accessibility barriers to inform infrastructure priorities
2. **Resource optimization**: Identify cost-effective deployment strategies through network analysis
3. **Equity focus**: Ensure investment prioritizes most isolated and underserved communities
4. **Community engagement**: Provide accessible visualizations and scorecards for local stakeholders
5. **Policy advocacy**: Generate empirical evidence for funding applications and policy discussions

---

## Resources & References

### OSMnx Documentation & Papers

**Primary Resources**:
- **OSMnx Documentation**: [https://osmnx.readthedocs.io/](https://osmnx.readthedocs.io/)
- **GitHub Repository**: [https://github.com/gboeing/osmnx](https://github.com/gboeing/osmnx)

**Key Academic Papers**:
- Boeing, G. (2017). "OSMnx: New methods for acquiring, constructing, analyzing, and visualizing complex street networks." *Computers, Environment and Urban Systems*, 65, 126-139. [DOI: 10.1016/j.compenvurbsys.2017.05.004](https://doi.org/10.1016/j.compenvurbsys.2017.05.004)
- Boeing, G. (2020). "Planarity and street network representation in urban form analysis." *Environment and Planning B: Urban Analytics and City Science*, 47(5), 855-869.
- Boeing, G. (2021). "Street Network Models and Indicators for Every Urban Area in the World." *Geographical Analysis*, 54(3), 519-535.

### Accessibility Analysis Research

**Transportation & Access**:
- Levinson, D. M., & Wu, H. (2020). "Towards a general theory of access." *Journal of Transport and Land Use*, 13(1), 129-158.
- Páez, A., Scott, D. M., & Morency, C. (2012). "Measuring accessibility: positive and normative implementations of various accessibility indicators." *Journal of Transport Geography*, 25, 141-153.

**Digital Equity & Accessibility**:
- Benda, N. C., et al. (2020). "Broadband Internet Access Is a Social Determinant of Health!" *American Journal of Public Health*, 110(8), 1123-1125.
- van Dijk, J. A. (2020). *The Digital Divide*. Polity Press.

### Broadband Infrastructure & Policy

**Federal Resources**:
- **FCC National Broadband Map**: [https://broadbandmap.fcc.gov/](https://broadbandmap.fcc.gov/)
- **NTIA Broadband Equity, Access, and Deployment (BEAD) Program**: [https://broadbandusa.ntia.doc.gov/funding-programs/broadband-equity-access-and-deployment-bead-program](https://broadbandusa.ntia.doc.gov/funding-programs/broadband-equity-access-and-deployment-bead-program)
- **USDA ReConnect Program**: Rural broadband funding resources

**Michigan-Specific**:
- **Michigan High-Speed Internet Office**: State broadband initiatives and data
- **Connect Michigan**: Broadband mapping and planning resources

### Network Analysis & Graph Theory

**Foundational Texts**:
- Barthélemy, M. (2011). "Spatial networks." *Physics Reports*, 499(1-3), 1-101.
- Newman, M. E. (2018). *Networks: An Introduction* (2nd ed.). Oxford University Press.
- Crucitti, P., Latora, V., & Porta, S. (2006). "Centrality measures in spatial networks of urban streets." *Physical Review E*, 73(3), 036125.

**Software Documentation**:
- **NetworkX**: [https://networkx.org/](https://networkx.org/) - Graph analysis in Python
- **GeoPandas**: [https://geopandas.org/](https://geopandas.org/) - Spatial data in Python
- **Folium**: [https://python-visualization.github.io/folium/](https://python-visualization.github.io/folium/) - Interactive mapping

### Urban Morphology & Spatial Analysis

**Key Research**:
- Batty, M. (2013). *The New Science of Cities*. MIT Press.
- Porta, S., Crucitti, P., & Latora, V. (2006). "The network analysis of urban streets: a primal approach." *Environment and Planning B*, 33(5), 705-725.

---

## Next Steps

{% include callout.html type="info" title="Getting Started" content="This research plan provides a comprehensive framework for integrating OSMnx capabilities with digital equity analysis. The phased approach allows for iterative development, community feedback, and adaptive refinement based on initial findings." %}

### Immediate Actions (Phase 1)
1. **Environment Setup**: Install Python packages and configure development environment
2. **Data Inventory**: Catalog available broadband coverage data and digital resource locations
3. **Pilot Selection**: Choose 2-3 EUP communities for initial analysis
4. **Stakeholder Engagement**: Connect with EUPConnect partners to refine research questions

### Future Opportunities
- **Expand Geographic Scope**: Apply methodology to other Michigan regions or nationwide
- **Multi-State Comparison**: Compare rural connectivity patterns across Upper Midwest
- **Temporal Analysis**: Track changes in accessibility as infrastructure deployment progresses
- **Integration with Other Data**: Incorporate health outcomes, economic indicators, educational attainment

### Collaboration Opportunities

This research benefits from partnerships with:
- **Academic Institutions**: MSU, Michigan Tech, Northern Michigan University
- **Regional Organizations**: EUPConnect Collaborative, UP regional planning commissions
- **State Agencies**: Michigan High-Speed Internet Office, MEDC
- **Community Organizations**: Libraries, digital literacy programs, tribal governments

---

## Contact for Research Collaboration

**Research Inquiries**: [jason@jasonkronemeyer.com](mailto:jason@jasonkronemeyer.com)  
**Areas of Interest**: Urban network analysis, digital equity, rural connectivity, spatial data science

---

*By integrating street network topology with broadband infrastructure analysis, we can develop more nuanced understanding of digital equity challenges and create more effective, community-centered solutions for expanding access in rural and underserved areas.*
