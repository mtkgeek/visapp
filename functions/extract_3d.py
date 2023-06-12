from branca.element import Template, MacroElement
from folium import IFrame
from nicegui import app, ui
import pandas as pd
import geopandas as gpd
import folium
from bs4 import BeautifulSoup
from lxml import html


app.add_static_files('/static', 'static')


def create_geojson():
    nuts2 = gpd.read_file('static/nuts.geojson')

    yields = pd.read_csv("static/potato_NL_train.csv", sep=",")
    yields = yields[["IDREGION", "FYEAR", "YIELD"]]
    yield_nuts2 = pd.merge(
        nuts2, yields, left_on="NUTS_ID", right_on="IDREGION")
    yield_nuts2_gdf = gpd.GeoDataFrame(yield_nuts2, geometry='geometry')
    yield_nuts2_gdf = yield_nuts2_gdf.to_crs(epsg=4326)
    yield_nuts2_gdf.to_file("static/output.geojson", driver='GeoJSON')


def readhtml3d():

    create_geojson()

    with open(r'static/map.html', "r") as f:
        page = f.read()
        map_html = page

        # Extract the script tags
        script_tags = []
        link_tags = []
        while '<script' in map_html:
            start = map_html.index('<script')
            end = map_html.index('</script>') + len('</script>')
            script_tags.append(map_html[start:end])
            map_html = map_html[:start] + map_html[end:]
        for i in script_tags:
            ui.add_head_html(i)

        while '<link' in map_html:
            start = map_html.index('<link')
            end = map_html.index('>') + len('>')
            link_tags.append(map_html[start:end])
            map_html = map_html[:start] + map_html[end:]
        for i in link_tags:
            ui.add_head_html(i)

        # Return the HTML string without the script tags and the script tags list
        return map_html
