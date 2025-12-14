from django.urls import path
from .views import login_view, logout_view, activity_logs

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('logs/', activity_logs, name='activity_logs'),

]
