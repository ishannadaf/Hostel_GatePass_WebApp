from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from students.models import Student
from gatein.models import GateIn
from gatepass.models import GatePass
from django.utils import timezone

@login_required(login_url='/login/')
def dashboard(request):
    context = {
        'role': request.user.role,
        'today': timezone.now().date()
    }

    # Common stats
    context['today_gatein'] = GateIn.objects.filter(date=context['today']).count()
    context['today_gatepass'] = GatePass.objects.filter(date=context['today']).count()

    # Admin-only stats
    if request.user.role == 'admin':
        context['total_students'] = Student.objects.count()

    return render(request, 'dashboard/dashboard.html', context)
