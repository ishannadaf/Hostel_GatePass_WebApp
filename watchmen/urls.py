from django.urls import path
from .views import add_watchman, watchman_list, watchman_edit, watchman_delete

urlpatterns = [
    path('add/', add_watchman, name='add_watchman'),
    path('', watchman_list, name='watchman_list'),
    path('edit/<int:id>/', watchman_edit, name='watchman_edit'),
    path('delete/<int:id>/', watchman_delete, name='watchman_delete'),
]
