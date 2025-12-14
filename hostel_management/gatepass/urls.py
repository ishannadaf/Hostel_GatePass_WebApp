from django.urls import path
from .views import gatepass_entry, gatepass_list

urlpatterns = [
    path('', gatepass_entry, name='gatepass'),
    path('records/', gatepass_list, name='gatepass_list'),
]
