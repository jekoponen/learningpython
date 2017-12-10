import folium
import pandas
from geopy.geocoders import Nominatim

nom=Nominatim(scheme="http")
map_centre=nom.geocode("Helsinki")

#a function returns color depending the type of location passed to the function
def type_to_colors(type):
    if type == "Private":
        return "orange"
    elif type == "Work":
        return "blue"
    elif type == "Hobbie":
        return "green"
    else:
        return 'red'
#a funtion returns color depending ot the integer population is passed to the function
def fcolor(population):
    if population < 10000000:
        return 'green'
    elif 10000000 <= population <100000000:
        return 'yellow'
    else:
        return 'red'

#create folium map object
map = folium.Map(location=[map_centre.latitude, map_centre.longitude], zoom_start=10, tiles="Mapbox Bright")

#create feateure group
fg_loc = folium.FeatureGroup(name="Locations")
#read coordinates and names from csv with pandas
crd_dataFrame = pandas.read_csv("resources/coordinates1.csv", sep=",")
#iterate trhough dataFrame. .values method returns dataframe as numpy.ndarray and it can be iterated with for loop
for row in crd_dataFrame.values:
    #values in csv is order: Name,latitude,longitude,Type
    fg_loc.add_child(folium.Marker(location=[row[1], row[2]], popup=row[0], icon=folium.Icon(color=type_to_colors(row[3]))))

#create an another feature group for population. population layer actually has only one object so it could be added as child directly, but let's create fG for consistensy
fg_pop = folium.FeatureGroup(name="Population")
#create GeoJson child object, this add polygon layer on the map and fillcolor of the countries are conditional to population
fg_pop.add_child(folium.GeoJson(data=open("resources/world.json", "r", encoding="utf-8-sig").read(),
style_function = lambda x: {'fillColor': fcolor(x['properties']['POP2005'])}))


#add FeatureGroup as a child to map object
map.add_child(fg_loc)
map.add_child(fg_pop)
#add Layer controller for the map. must be added after all user controllable layers are added. see feature FeatureGroup
map.add_child(folium.LayerControl())
map.save("templates/Map1.html")
