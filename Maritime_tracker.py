import folium

# Create base map centered in Southeast Asia
map = folium.Map(location=[10,110], zoom_start=4)

# Example vessels
vessels = [
    {"name": "Cargo Ship A", "lat": 1.2, "lon": 103.8},
    {"name": "Oil Tanker B", "lat": 12.5, "lon": 121.0},
    {"name": "Container Ship C", "lat": 22.8, "lon": 114.2}
]

# Add markers to the map
for vessel in vessels:
    folium.Marker(
        location=[vessel["lat"], vessel["lon"]],
        popup=vessel["name"]
    ).add_to(map)

# Save map
map.save("maritime_map.html")

print("Map created!")
