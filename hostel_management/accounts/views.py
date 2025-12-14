from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.role == 'admin':
                return redirect('dashboard')
            else:
                return redirect('gatein')
        else:
            return render(request, 'auth/login.html', {'error': 'Invalid Credentials'})

    return render(request, 'auth/login.html')
