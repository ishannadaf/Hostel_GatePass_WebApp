from django.shortcuts import render, redirect, get_object_or_404
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



@role_required('admin')
def watchman_edit(request, id):
    watchman = get_object_or_404(User, id=id, role='watchman')

    if request.method == 'POST':
        watchman.first_name = request.POST.get('first_name', watchman.first_name)
        watchman.last_name = request.POST.get('last_name', watchman.last_name)
        watchman.username = request.POST.get('username', watchman.username)

        if request.POST.get('password'):
            watchman.set_password(request.POST.get('password'))

        watchman.save()
        return redirect('/watchmen/')

    return render(request, 'watchmen/watchman_edit.html', {'watchman': watchman})


@role_required('admin')
def watchman_delete(request, id):
    watchman = get_object_or_404(User, id=id, role='watchman')

    if request.method == 'POST':
        watchman.delete()
        return redirect('/watchmen/')

    return render(request, 'watchmen/watchman_delete.html', {
        'watchman': watchman
    })
