from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/', category, name='category'),
    path('search', serach_product, name='search'),
    path('autosuggest/', autosuggest, name='autosuggest'),

    
]
