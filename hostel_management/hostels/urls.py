from django.urls import path
from .views import add_hostel, hostel_list

urlpatterns = [
    path('add/', add_hostel, name='add_hostel'),
    path('', hostel_list, name='hostel_list'),
]
