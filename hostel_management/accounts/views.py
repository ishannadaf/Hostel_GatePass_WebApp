from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import ActivityLog
from accounts.decorators import role_required

def login_view(request):
    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/dashboard/')
        else:
            error = "Invalid username or password"

    return render(request, 'auth/login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')

@role_required('admin')
def activity_logs(request):
    logs = ActivityLog.objects.all().order_by('-timestamp')[:200]
    return render(request, 'accounts/activity_logs.html', {
        'logs': logs
    })