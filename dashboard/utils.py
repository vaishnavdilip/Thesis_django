import pandas as pd 
import numpy as np
from py2neo import Graph
import plotly.express as px
import plotly.graph_objects as go

graph = Graph("bolt://localhost:7687", auth=("neo4j", "neo4jneo4j"))

