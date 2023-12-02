import pandas as pd 
import numpy as np
from py2neo import Graph
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyo

graph = Graph("bolt://localhost:7687", auth=("neo4j", "neo4jneo4j"))

def sector_dist():
    query = """
    MATCH (c:Company)
    RETURN c.sector as Sector, count(c) as count
    """

    a = graph.run(query).to_data_frame()

    fig = px.pie(a, values='count', names='Sector', title='Sector distribution', height=500, width=700)
    plot_html = pyo.plot(fig, output_type='div')

    return plot_html

def supplier_year_dist():
    query = """
    MATCH ()-[r:SUPPLIES_TO]->()
    RETURN date(r.date).year as Year, count(r) as count
    """
    
    a = graph.run(query).to_data_frame()

    fig = px.bar(a, x='Year', y='count',  height=500, width=700)

    fig.update_layout(
        title='Number of supplier relations per year',
        xaxis_title='Year',
        yaxis_title='Number of supplier relations',
    )

    plot_html = pyo.plot(fig, output_type='div')
    return plot_html

def competes_year_dist():
    query = """
    MATCH ()-[r:COMPETES]->()
    RETURN date(r.date).year as Year, count(r) as count
    """

    a = graph.run(query).to_data_frame()

    fig = px.bar(a, x='Year', y='count',  height=500, width=700)

    fig.update_layout(
        title='Number of supplier relations per year',
        xaxis_title='Year',
        yaxis_title='Number of supplier relations',
    )

    plot_html = pyo.plot(fig, output_type='div')
    return plot_html
def partners_year_dist():
    query = """
    MATCH ()-[r:PARTNERS]->()
    RETURN date(r.date).year as Year, count(r) as count
    """

    a = graph.run(query).to_data_frame()
    fig = px.bar(a, x='Year', y='count',  height=500, width=700)

    fig.update_layout(
        title='Number of supplier relations per year',
        xaxis_title='Year',
        yaxis_title='Number of supplier relations',
    )

    plot_html = pyo.plot(fig, output_type='div')
    return plot_html

def country_dist():
    query = """
    MATCH (c:Company)
    RETURN c.country_code as country, count(c) as count
    """

    a = graph.run(query).to_data_frame()

    fig = px.choropleth(a, locations="country",
                    color="count",
                    hover_name="country", 
                    color_continuous_scale=px.colors.sequential.Plasma,
                    height=500, width=1000,)

    fig.update_layout(
        coloraxis_colorbar=dict(
        title="Number of companies per country",
        len=1
        ),
        title_text = 'Availability of company data based on country'
    )

    plot_html = pyo.plot(fig, output_type='div')
    return plot_html
