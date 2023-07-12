"""Defines URL patterns for vbm_app."""

from django.urls import path
from . import views
app_name = 'vbm_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # URI bruteforce page
    path('uris', views.bruteURI, name='bruteURI'),
    
    # Request bruteforce page
    path('reqs', views.bruteReqs, name='bruteReqs'),
]