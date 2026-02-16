"""
This script reproduces the interactive map pipeline as a tutorial.  It loads the E-Rate recipients dataset,
applies name and coordinate corrections, adds a custom Energy Lab marker, creates a Carto Positron
basemap with graduation-cap/building icons color coded by entity type, adds a legend including the
Energy Lab, puts a title banner at the top, overlays a logo in the upper-right, and saves the map
as an HTML file.
"""

import pandas as pd
import folium
from branca.element import Element
import base64

# Read the Excel file.  Make sure the file is in the same directory as this script or set the correct path.
excel_file = 'E-Rate_Recipient_Details_And_Commitments_20251203.xlsx'
print(f'Reading dataset from {excel_file}...')
df = pd.read_excel(excel_file, engine='openpyxl')

# Apply name/coordinate corrections
# Known coordinate fixes: if these names appear in the data, override the provided coordinates.
fixes = {
    'Ojibwe Charter School': (46.450085, -84.60143),
    'Malcolm School': (46.423161, -84.35593),
    'Sault Transportation Facility': (46.491341, -84.329903),
}
for name, (lat, lon) in fixes.items():
    mask = df['Recipient Entity Name'].str.contains(name, case=False, na=False)
    if mask.any():
        df.loc[mask, ['Recipient Latitude', 'Recipient Longitude']] = (lat, lon)

# Rename and update coordinates for Sault High School (and variants)
mask_high = df['Recipient Entity Name'].str.contains('Sault High School', case=False, na=False)
if mask_high.any():
    df.loc[mask_high, 'Recipient Entity Name'] = 'Sault Area Public Schools'
    df.loc[mask_high, ['Recipient Latitude', 'Recipient Longitude']] = (46.478283, -84.343873)
mask_high2 = df['Recipient Entity Name'].str.contains('Sault Area High School', case=False, na=False)
if mask_high2.any():
    df.loc[mask_high2, 'Recipient Entity Name'] = 'Sault Area Public Schools'
    df.loc[mask_high2, ['Recipient Latitude', 'Recipient Longitude']] = (46.478283, -84.343873)

# Rename middle school entries to elementary
mask_mid = df['Recipient Entity Name'].str.contains('Sault Area Middle School|Sault Middle School', case=False, na=False)
if mask_mid.any():
    df.loc[mask_mid, 'Recipient Entity Name'] = 'Sault Elementary'

# Drop entries with missing coordinates before mapping
df = df.dropna(subset=['Recipient Latitude', 'Recipient Longitude'])

# Create the map centered at the average latitude and longitude of the data
center = [df['Recipient Latitude'].mean(), df['Recipient Longitude'].mean()]
map_obj = folium.Map(location=center, zoom_start=8, tiles='CartoDB positron')

# Create a color mapping for each unique entity type
types = df['Recipient Entity Type'].dropna().unique().tolist()
palette = ['red','blue','green','purple','orange','darkred','lightred','beige','darkblue','darkgreen']
color_map = {types[i]: palette[i % len(palette)] for i in range(len(types))}

# Add markers for each recipient
for _, row in df.iterrows():
    # Get the BEN, if present
    ben = ''
    if pd.notnull(row.get('Recipient Entity Number')):
        try:
            ben = str(int(row['Recipient Entity Number']))
        except Exception:
            ben = str(row['Recipient Entity Number'])
    popup_text = f"{row['Recipient Entity Name']}<br>Type: {row['Recipient Entity Type']}<br>BEN: {ben}"
    # Determine icon based on type: use 'graduation-cap' for instructional, 'building' for non-instructional (type string contains 'non')
    t = str(row['Recipient Entity Type']).lower() if pd.notnull(row['Recipient Entity Type']) else ''
    icon_type = 'building' if 'non' in t else 'graduation-cap'
    icon_color = color_map.get(row['Recipient Entity Type'], 'black')
    icon = folium.Icon(icon=icon_type, prefix='fa', color=icon_color)
    folium.Marker(location=[row['Recipient Latitude'], row['Recipient Longitude']], icon=icon, popup=folium.Popup(popup_text, max_width=300)).add_to(map_obj)

# Add a custom marker for the Energy Lab
lab_coords = (46.489843, -84.35964)
lab_name = 'Cloverland Energy Technology Research and Development Lab'
folium.Marker(location=lab_coords, icon=folium.Icon(icon='bolt', prefix='fa', color='orange'), popup=folium.Popup(lab_name, max_width=300)).add_to(map_obj)

# Build the legend HTML including the Energy Lab entry
legend_html = '<div style="position: fixed; bottom: 50px; left: 50px; width: 220px; z-index:9999; font-size:14px; background-color: white; opacity: 0.8; padding: 10px;">'
legend_html += '<b>Entity Types</b><br>'
for t in types:
    col = color_map.get(t, 'black')
    legend_html += f'<i style="background:{col};width:10px;height:10px;display:inline-block;margin-right:5px;"></i>{t}<br>'
# Add Energy Lab legend entry
legend_html += '<i style="background:orange;width:10px;height:10px;display:inline-block;margin-right:5px;"></i>Energy Lab<br>'
legend_html += '</div>'
map_obj.get_root().html.add_child(Element(legend_html))

# Add the title banner at top
title_html = '<div style="position: fixed; top: 0; left: 0; right: 0; text-align: center; font-size: 20px; font-weight: bold; background-color: white; padding: 5px; z-index: 1000;">Connecting the EUPSchools to Each Other</div>'
map_obj.get_root().html.add_child(Element(title_html))

# Add the logo overlay; set z-index higher than the title so it appears on top
with open('EUP Connect Simple.jpg', 'rb') as f:
    logo_data = base64.b64encode(f.read()).decode('utf-8')
logo_html = f'<div style="position: fixed; top: 10px; right: 10px; z-index: 1001; background: white; padding:5px; border-radius:5px;"><img src="data:image/jpeg;base64,{logo_data}" style="width:80px;"></div>'
map_obj.get_root().html.add_child(Element(logo_html))

# Save the map as an HTML file
output_html = 'recipients_map_tutorial.html'
print(f'Saving map to {output_html}...')
map_obj.save(output_html)
