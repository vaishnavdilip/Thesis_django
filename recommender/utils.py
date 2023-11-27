import pandas as pd
import numpy as np
from py2neo import Graph
import plotly.express as px
import geopandas as gpd
from shapely.geometry import Point
import plotly.offline as pyo

# graph = Graph('bolt://localhost:7687', auth = ('neo4j', 'neo4jneo4j'))


def recommender(company_id, n=10):
    graph = Graph("bolt://localhost:7687", auth=("neo4j", "neo4jneo4j"))

    query = f"""
    MATCH (a:Company {{id: "{company_id}"}})-[:PARTNERS]-(b:Company)
    RETURN b.id as id, count(*) as count
    ORDER BY count DESC
    LIMIT {n}
    """

    query2 = f"""
    MATCH (s:Company)-[:SUPPLIES_TO]->(c:Company {{name: "{company_id}"}})-[:COMPETES]-(d:Company)<-[l:SUPPLIES_TO]-(t:Company)
    WHERE c.name <> t.name
    WITH c, t,d
    RETURN DISTINCT t.name as target, t.point as target_loc, c.name as comp_name, c.point as comp_loc, point.distance(c.point, t.point) as distance
    ORDER BY distance ASC
    LIMIT {n}
    """

    return graph.run(query2).to_data_frame()


def plotter(company_id, n=10):
    graph = Graph("bolt://localhost:7687", auth=("neo4j", "neo4jneo4j"))

    df = recommender(company_id, n)

    source = {
        "lat": list(set(df["comp_loc"].apply(lambda x: x.latitude))),
        "lon": list(set(df["comp_loc"].apply(lambda x: x.longitude))),
        "name": list(set(df["comp_name"])),
        "type": ["source"]
    }

    data = {
        "lat": list(df["target_loc"].apply(lambda x: x.latitude)) + source['lat'],
        "lon": list(df["target_loc"].apply(lambda x: x.longitude)) + source['lon'],
        "name": list(df["target"]) + source['name'],
        "type": ["options"]*len(df['target']) + source['type']
    }

    # Create a GeoDataFrame from the data
    geometry = [Point(lon, lat) for lon, lat in zip(data["lon"], data["lat"])]
    gdf = gpd.GeoDataFrame(data, geometry=geometry)

    fig = px.scatter_geo(
        gdf,
        lat=gdf.geometry.y,
        lon=gdf.geometry.x,
        hover_name="name",
        scope="world",
        color="type",
        projection="orthographic",
    )

    plot_html = pyo.plot(fig, output_type='div')

    return plot_html

    # fig.show()
