import folium
import pandas
import geocoder

def setColor(elevation):
    if elevation<1000:
        return 'green'
    elif elevation<3000:
        return 'orange'
    else:
        return 'red'


mygeoposition = geocoder.ip('me')

df = pandas.read_csv('Volcanoes.txt')

lat = list(df['LAT'])
lon = list(df['LON'])
elev = list(df['ELEV'])

html = """<h4>Volcano information:</h4>
Height: %s m
"""

map = folium.Map(location=mygeoposition.latlng,zoom_start=6, tiles='Stamen Terrain')

fgv = folium.FeatureGroup(name='Volcanos')
fgc = folium.FeatureGroup(name='Countries')

fgc.add_child(folium.GeoJson('world-countries.json', 
style_function=lambda x:{'fillColor':'green' if x['properties']['name']=='Russia' else 'red'}))

for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    # fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe), icon=folium.Icon(color=setColor(el), icon='star', prefix='fa',)))
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=10, popup=folium.Popup(iframe), fill_color=setColor(el), fill_opacity=1))

map.add_child(fgv)
map.add_child(fgc)

map.add_child(folium.LayerControl()) 

map.save('Map1.html')