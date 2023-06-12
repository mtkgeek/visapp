from branca.element import Template, MacroElement
from folium import IFrame
from nicegui import app, ui
import pandas as pd
import geopandas as gpd
import folium
from bs4 import BeautifulSoup


app.add_static_files('/static', 'static')


def readcsv():
    nuts2 = gpd.read_file('static/nuts.geojson')

    yields = pd.read_csv("static/potato_NL_train.csv", sep=",")
    yields = yields[["IDREGION", "FYEAR", "YIELD"]]
    yield_nuts2 = pd.merge(
        nuts2, yields, left_on="NUTS_ID", right_on="IDREGION")
    yield_nuts2_gdf = gpd.GeoDataFrame(yield_nuts2, geometry='geometry')
    yield_nuts2_gdf = yield_nuts2_gdf.to_crs(epsg=4326)

    # Center the map on the Netherlands
    location = [52.1326, 7.9913]
    map = folium.Map(location=location, tiles="OpenStreetMap", zoom_start=7)

    # Create a GeoJsonTooltip object
    tooltip = folium.features.GeoJsonTooltip(
        fields=["NUTS_ID", "FYEAR", "YIELD"],
        aliases=["NUTS ID:", "Fiscal Year:", "Yield:"],
        localize=False
    )

    # Add the GeoJSON layer to the map
    choropleth = folium.Choropleth(
        geo_data=yield_nuts2_gdf,
        name="Potato Yields",
        data=yields,
        columns=["IDREGION", "YIELD"],
        key_on="feature.properties.NUTS_ID",
        fill_color="BuPu",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Yield (t/ha)",
    )

    # Add the tooltip to the choropleth
    choropleth.geojson.add_child(tooltip)

    # Add the choropleth to the map
    choropleth.add_to(map)

    folium.LayerControl().add_to(map)

    # Render the map to HTML
    map_html = map._repr_html_()

    # Extract the script tags
    script_tags = []
    while '<script' in map_html:
        start = map_html.index('<script')
        end = map_html.index('</script>') + len('</script>')
        script_tags.append(map_html[start:end])
        map_html = map_html[:start] + map_html[end:]
    for i in script_tags:
        ui.add_head_html(i)

    # Return the HTML string without the script tags and the script tags list
    return map_html
