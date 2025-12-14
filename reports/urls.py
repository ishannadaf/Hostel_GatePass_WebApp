from django.urls import path
from .views import reports_home, daily_report, weekly_report

urlpatterns = [
    path('', reports_home, name='reports_home'),
    path('daily/', daily_report, name='daily_report'),
    path('weekly/', weekly_report, name='weekly_report'),
]
