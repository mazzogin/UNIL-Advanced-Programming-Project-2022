#import libraries
import pandas as pd
import numpy as np
import json
import warnings
import pyproj
import pyproj.network
from pyproj import CRS, Transformer
import shapely
import shapely.geos
import altair as alt #pip3 install altair
import altair_saver
import geopandas as gpd #pip3 install geopandas
from pyproj import Transformer
from matplotlib import pyplot as plt


#import data
df = pd.read_excel('Heatmap/data.xlsx', sheet_name='Sheet1', index_col=0)
df['Zip_Code'] = df['Zip_Code'].replace({'0 21': '1000', '0 25': '1000', '0 26':'1000'})
df['Zip_Code'] = df['Zip_Code'].astype('float')

#Calcule price mean by zipcode
pricebyzip = df[['Zip_Code', 'Price']].groupby(['Zip_Code'], as_index=False).mean()

#load shapefile of zipcodes
gdf = gpd.read_file('Heatmap/PLZO_SHP_LV95/PLZO_PLZ.shp')
gdf = gdf.to_crs(epsg = 4326)


#get only wanted zip codes for the lausanne area
great_lausanne = [1000, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 
            1010, 1012, 1015, 1018, 1020, 1022, 1023, 1024, 1025, 
            1027, 1028, 1029, 1030, 1031, 1032, 1033, 1036, 1037, 
            1052, 1053, 1054, 1055, 1066, 1073, 1081, 1090, 1091,
            1092, 1093, 1094, 1095, 1096, 1097, 1098, 1121, 1302]

gdf_laus = gdf[gdf['PLZ'].isin(great_lausanne)]

#Merge geographical data with average price by zip code to create geopanda dataframe
gdf_laus = gdf_laus.merge(pricebyzip, left_on='PLZ', right_on='Zip_Code')
########
#gdf_laus.to_excel('pleasework.xlsx')

#display zip_code on map
gdf_laus['x'] = gdf_laus['geometry'].centroid.x
gdf_laus['y'] = gdf_laus['geometry'].centroid.y


#adapt data to Create choropleth map 
json_laus = json.loads(gdf_laus.to_json())
alt_laus = alt.Data(values = json_laus['features'])

#Make map with altair
alt_pricebyzip = alt.Chart(alt_laus).mark_geoshape(
    stroke = 'blue'
).encode(
    latitude = 'properties.y:Q',
    longitude = 'properties.x:Q',
    color = 'properties.pricebyzip:Q'
).properties(
    width = 400,
    height = 500
)

alt_pricebyzip
#alt_pricebyzip # to display the map

text  = alt.Chart(alt_laus).mark_text(
        
).encode(
    longitude = 'properties.x:Q',
    latitude = 'properties.y:Q',
    text = 'properties.Zip_Code:Q',
)

#display both map with prices and text
chart = alt_pricebyzip + text
chart
altair_saver.save(chart, "chart.png")
chart.save('test2.html')