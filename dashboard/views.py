from django.shortcuts import render
from django.http import JsonResponse
# from dashboard.models import Order
from django.core import serializers
from .utils import sector_dist, supplier_year_dist, competes_year_dist, partners_year_dist, country_dist

# Create your views here.

def dashboard_with_pivot(request):
    sector_plot = sector_dist()
    competes_plot = competes_year_dist()
    partner_plot = partners_year_dist()
    supplier_plot = supplier_year_dist()
    country_plot = country_dist()
    return render(request, 'dashboard_with_pivot.html', {'sector_plot' : sector_plot, 'competes_plot' : competes_plot, 'partner_plot' : partner_plot, 'supplier_plot' : supplier_plot, 'country_plot' : country_plot})

# def pivot_data(request):
#     dataset = Order.objects.all()
#     data = serializers.serialize('json', dataset)
#     return JsonResponse(data, safe=False)