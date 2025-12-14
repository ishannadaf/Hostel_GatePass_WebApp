from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import ActivityLog
from accounts.decorators import role_required
from django.contrib.auth import get_user_model
from django.contrib import messages

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
    

User = get_user_model()
    
def admin_signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm_password")

        if password != confirm:
            messages.error(request, "Passwords do not match")
            return redirect("admin_signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("admin_signup")

        user = User.objects.create_user(
            username=username,
            password=password
        )
        user.role = "admin"
        user.is_staff = True
        user.is_superuser = True
        user.save()

        messages.success(request, "Admin account created. Please login.")
        return redirect("login")

    return render(request, "accounts/admin_signup.html")