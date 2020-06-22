import folium
import pandas as pd

df = pd.read_csv("original.txt")
#print(df)
lat = list(df["LAT"])
lon = list(df["LON"])
location1 = list(df["LOCATION"])
elev = list(df["ELEV"])


html="""<h4>Volcano information</h4>
Height: %s m
"""

def color_producer(elevation):
    if elevation<1000:
        return "green"
    elif 1000<=elevation<3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location=[38.8,-99.09],zoom_start=6,tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanos")

fgp = folium.FeatureGroup(name="Population")

for lt, ln, el in zip(lat,lon,elev):
    #iframe = folium.iframe(html=html % str(el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius = 6, popup=str(el)+" m", fill_color=color_producer(el), color="grey", fill_opacity=0.7 ))


fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(), style_function= lambda x : {'fillColor':'green' if x ['properties']['POP2005']<10000000
else 'orange' if 10000000 <= x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")