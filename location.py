import googlemaps
from datetime import datetime

# Initialize the client with your API key
gmaps = googlemaps.Client(key='YOUR_API_KEY')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Extract latitude and longitude from the result
location = geocode_result[0]['geometry']['location']
lat, lng = location['lat'], location['lng']

print(f'Latitude: {lat}, Longitude: {lng}')
