from django.urls import path
from .views import gatein_entry, gatein_list

urlpatterns = [
    path('', gatein_entry, name='gatein'),
    path('records/', gatein_list, name='gatein_list'),
]
