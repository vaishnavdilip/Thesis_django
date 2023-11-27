from django.urls import path
from . import views

urlpatterns = [
    path('recommender/', views.index, name='index2'),
    path('recommend/', views.recommend, name='recommend'),
]