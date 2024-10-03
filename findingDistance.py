import geopy.distance

# importing geopy library and Nominatim class
from geopy.geocoders import Nominatim

# calling the Nominatim tool and create Nominatim class
loc = Nominatim(user_agent="Geopy Library")

#Getting start location
start = input("Please Provide Street Address You're Starting From:")
type = input("What type (Tent/Cabin/etc...):")
nights = input("How Many Nights:")
date = input("What Is Your Start Date (MM/DD/YYYY):")


# entering the location name
getLoc = loc.geocode(start)

coords_1 = (getLoc.latitude, getLoc.longitude)

for each:
  coords_2 = (52.406374, 16.9251681)
 
  print(geopy.distance.geodesic(coords_1, coords_2).miles)
