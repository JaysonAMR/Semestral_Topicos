import json
import pandas as pd
import requests
import plotly.express as px
df=pd.read_csv("C:\\Users\\jayso\\Documents\\GitHub\\Semestral_Topicos\\MexicoData.csv")
repo_url = 'https://raw.githubusercontent.com/angelnmara/geojson/master/mexicoHigh.json' #Archivo GeoJSON
mx_regions_geo = requests.get(repo_url).json()

fig = px.choropleth(data_frame=df, 
                    geojson=mx_regions_geo, 
                    locations='Estado', # nombre de la columna del Dataframe
                    featureidkey='properties.name',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
                    color='Casos', #El color depende de las cantidades
                    color_continuous_scale="greens", #greens
                    #scope="north america"
                   )
fig.update_geos(showcountries=False, showcoastlines=True, showland=False, fitbounds="locations")



fig.show()