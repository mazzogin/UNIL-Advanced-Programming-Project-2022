#import libraries
import pandas as pd
import numpy as np
import json
import warnings
import pyproj
import pyproj.network
import shapely
import shapely.geos
import altair as alt #pip3 install altair
import geopandas as gpd #pip3 install geopandas


#import data
df = pd.read_excel('/Users/admin/Desktop/2ndGUI/data.xlsx', sheet_name='Sheet1', index_col=0)

#Calcule price mean by zipcode
pricebyzip = df.groupby('Zip_Code')[['Price']].mean().reset_index

#load shapefile of zipcodes
gdf = gpd.read_file('/Users/admin/Desktop/2ndGUI/PLZO_SHP_LV95/PLZO_PLZ.shp')

#Convert coordinate system
gdf = gdf.to_crs({'init': 'espg:4326'})

#get only wanted zip codes for the lausanne area
great_lausanne = [1000, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 
            1010, 1012, 1015, 1018, 1020, 1022, 1023, 1024, 1025, 
            1027, 1028, 1029, 1030, 1031, 1032, 1033, 1036, 1037, 
            1052, 1053, 1054, 1055, 1066, 1073, 1081, 1090, 1091,
            1092, 1093, 1094, 1095, 1096, 1097, 1098, 1121, 1302]
gdf_laus = gdf[gdf['PLZ'].isin(great_lausanne)]

#Merge geographical data with average price by zip code to create geopanda dataframe
gdf_laus = gdf_laus.merge(pricebyzip, left_on='PLZ', right_on='ZipCode')

#adapt data to Create choropleth map 
json_laus = json.loads(gdf_laus.to_json())
alt_laus = alt.Data(values = json_laus['features'])

#Make map with altair
alt_pricebyzip = alt.Chart(alt_laus).mark_geoshape(
    stroke = 'white'
).encode(
    latitude = 'properties.y:Q',
    longitude = 'properties.x:Q',
    color = 'properties.pricebyzip:Q'
).properties(
    width = 400,
    height = 500
)
#alt_pricebyzip # to display the map

#display zip_code on map
gdf_laus['x'] = gdf_laus['geometry'].centroid.x
gdf_laus['y'] = gdf_laus['geometry'].centroid.y

text  = alt.Chart(alt_laus).mark_text(
        
).encode(
    longitude = 'properties.x:Q',
    latitude = 'properties.y:Q',
    text = 'properties.Zip_Code:Q',
)

#display both map with prices and text
chart = alt_pricebyzip + text
chart