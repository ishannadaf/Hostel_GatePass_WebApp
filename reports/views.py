from django.shortcuts import render
from gatein.models import GateIn
from gatepass.models import GatePass
from django.utils import timezone
from accounts.decorators import role_required
from datetime import timedelta

@role_required('admin')
def reports_home(request):
    return render(request, 'reports/reports_home.html')


@role_required('admin')
def daily_report(request):
    today = timezone.now().date()

    gatein = GateIn.objects.filter(date=today)
    gatepass = GatePass.objects.filter(date=today)

    return render(request, 'reports/daily_report.html', {
        'gatein': gatein,
        'gatepass': gatepass,
        'date': today
    })


from datetime import timedelta

@role_required('admin')
def weekly_report(request):
    today = timezone.now().date()
    start_date = today - timedelta(days=7)

    gatein = GateIn.objects.filter(date__range=[start_date, today])
    gatepass = GatePass.objects.filter(date__range=[start_date, today])

    return render(request, 'reports/weekly_report.html', {
        'gatein': gatein,
        'gatepass': gatepass,
        'start': start_date,
        'end': today
    })




@role_required('admin')
def weekly_report(request):
    today = timezone.now().date()
    start_date = today - timedelta(days=7)

    gatein = GateIn.objects.filter(date__range=[start_date, today])
    gatepass = GatePass.objects.filter(date__range=[start_date, today])

    return render(request, 'reports/weekly_report.html', {
        'gatein': gatein,
        'gatepass': gatepass,
        'start': start_date,
        'end': today
    })
