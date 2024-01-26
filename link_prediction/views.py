from django.shortcuts import render
from .utils import *
# Create your views here.

def index(request):

    table = plot_table()
    prediction_plot = plot_connections()
    

    return render(request, 'link_prediction.html', {'table': table, 'prediction_plot': prediction_plot})