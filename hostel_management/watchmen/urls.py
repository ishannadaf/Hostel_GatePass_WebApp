from django.urls import path
from .views import add_watchman, watchman_list

urlpatterns = [
    path('add/', add_watchman, name='add_watchman'),
    path('', watchman_list, name='watchman_list'),
]
