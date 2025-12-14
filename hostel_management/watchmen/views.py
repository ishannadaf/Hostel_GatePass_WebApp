from django.shortcuts import render, redirect
from .models import Watchman
from accounts.models import User
from accounts.decorators import role_required

@role_required('admin')
def add_watchman(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            role='watchman'
        )

        Watchman.objects.create(
            user=user,
            name=request.POST['name'],
            mobile=request.POST['mobile'],
            assigned_hostel=request.POST['assigned_hostel']
        )

        return redirect('watchman_list')

    return render(request, 'watchmen/add_watchman.html')


@role_required('admin')
def watchman_list(request):
    watchmen = Watchman.objects.all()
    return render(request, 'watchmen/watchman_list.html', {'watchmen': watchmen})
