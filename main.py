import phonenumbers
import folium
# from test import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

import random
import pyautogui

number = pyautogui.prompt("Enter a Phone Number (eg.+254712345678) : ")

key = 'f0daa136d83f48f29e85601b69d9baa3'

# getting the country
someNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(someNumber, "en")
print(yourLocation)


# getting the service provider
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))


# getting the location
geocoder = OpenCageGeocode(key)
query = str(yourLocation)
results =  geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)
folium.Marker([lat, lng],popup= yourLocation).add_to((myMap))

# save map in html file
myMap.save('myLocation.html')