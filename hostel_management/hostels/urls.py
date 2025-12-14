from django.urls import path
from .views import add_hostel, hostel_list, hostel_edit, hostel_delete

urlpatterns = [
    path('add/', add_hostel, name='add_hostel'),
    path('', hostel_list, name='hostel_list'),
    path('edit/<int:id>/', hostel_edit, name='hostel_edit'),
    path('delete/<int:id>/', hostel_delete, name='hostel_delete'),
]
