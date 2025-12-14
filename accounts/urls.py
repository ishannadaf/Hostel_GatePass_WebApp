from django.urls import path
from .views import login_view, logout_view, activity_logs, admin_signup

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('logs/', activity_logs, name='activity_logs'),
    path("signup/", admin_signup, name="admin_signup"),
]
