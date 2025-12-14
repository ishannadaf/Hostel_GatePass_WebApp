from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.timezone import now
from datetime import timedelta

from gatein.models import GateIn
from gatepass.models import GatePass
from students.models import Student

@login_required(login_url='/login/')
def dashboard(request):
    today = now().date()

    labels = []
    gatein_data = []
    gatepass_data = []

    for i in range(6, -1, -1):
        day = today - timedelta(days=i)
        labels.append(day.strftime('%d %b'))

        gatein_data.append(
            GateIn.objects.filter(date=day).count()
        )

        gatepass_data.append(
            GatePass.objects.filter(date=day).count()
        )

    context = {
        'today': today,
        'today_gatein': GateIn.objects.filter(date=today).count(),
        'today_gatepass': GatePass.objects.filter(date=today).count(),
        'total_students': Student.objects.count(),

        'labels': labels,
        'gatein_data': gatein_data,
        'gatepass_data': gatepass_data,
    }

    return render(request, 'dashboard/dashboard.html', context)
