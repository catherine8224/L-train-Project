#!/usr/bin/env python3
# -*-coding: utf-8 -*-

import pandas as pd
import folium #import the folium package for making maps
from scipy.spatial import Voronoi, voronoi_plot_2d

#File with library locations in NYC:
libs = pd.read_csv('DOITT_SUBWAY_STATION_01_13SEPT2010.csv')

#Create a list to hold coordinates and popups:
coords = []
popups = []
icons = []

#Create map object, focused on NYC
mapLibrary = folium.Map(location=[40.75, -73.9], tiles="Cartodb Positron", zoom_start=10)

#For each row in the CSV, pull out the latitude, longitude, and name of the library:
for index, row in libs.iterrows():
    words = row['the_geom'].split(" ")
    lat = float(words[2][:-1])
    lon = float(words[1][1:])
    name = row['NAME']
    #Add [lat,lon] to list of coordinates:
    coords.append([lat, lon])
    #Add a marker to the map:
    popup=folium.Popup(libs['NAME'], parse_html=True)
    folium.Marker([lat,lon],popup).add_to(mapLibrary)
    #print("Processing:", name)
#Use scipy to make the voronoi diagram:
vor = Voronoi(coords)
    
#Plot with matplotlib to check that it's working:              
import matplotlib.pyplot as plt
fig = voronoi_plot_2d(vor)
plt.show()

#Use geojson file to write out the features
from geojson import FeatureCollection, Feature, Polygon

#The output file, to contain the Voronoi diagram we computed:
vorJSON = open('SwyVor.json', 'w')
point_voronoi_list = []
feature_list = []
for region in range(len(vor.regions)-1):
#for region in range(9):    
    vertex_list = []
    for x in vor.regions[region]:
        #Not sure how to map the "infinite" point, so, leave off those regions for now:
        if x == -1:
            break;
        else:
            #Get the vertex out of the list, and flip the order for folium:
            vertex = vor.vertices[x]
            vertex = (vertex[1], vertex[0])
        vertex_list.append(vertex)
    #Save the vertex list as a polygon and then add to the feature_list:
    polygon = Polygon([vertex_list])
    feature = Feature(geometry=polygon, properties={})
    feature_list.append(feature)

#Write the features to the new file:
feature_collection = FeatureCollection(feature_list)
print (feature_collection, file=vorJSON)
vorJSON.close()

#Add the voronoi layer to the map:
mapLibrary.choropleth(geo_data = 'SwyVor.json', fill_color="BuPu",
            fill_opacity=0.01, line_opacity=0.5)
mapLibrary.save(outfile='Subway.html')
