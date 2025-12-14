from django.shortcuts import render, redirect, get_object_or_404
from .models import Hostel
from accounts.decorators import role_required

@role_required('admin')
def add_hostel(request):
    if request.method == 'POST':
        Hostel.objects.create(
            hostel_name=request.POST['hostel_name'],
            total_rooms=request.POST['total_rooms'],
            warden_name=request.POST['warden_name'],
            contact_no=request.POST['contact_no']
        )
        return redirect('hostel_list')

    return render(request, 'hostels/add_hostel.html')


@role_required('admin')
def hostel_list(request):
    hostels = Hostel.objects.all()
    return render(request, 'hostels/hostel_list.html', {'hostels': hostels})


@role_required('admin')
def hostel_edit(request, id):
    hostel = get_object_or_404(Hostel, id=id)

    if request.method == 'POST':
        hostel.name = request.POST.get('name', hostel.name)
        hostel.capacity = request.POST.get('capacity', hostel.capacity)
        hostel.address = request.POST.get('address', hostel.address)
        hostel.save()

        return redirect('/hostels/')

    return render(request, 'hostels/hostel_edit.html', {'hostel': hostel})

@role_required('admin')
def hostel_delete(request, id):
    hostel = get_object_or_404(Hostel, id=id)

    if request.method == 'POST':
        hostel.delete()
        return redirect('/hostels/')

    return render(request, 'hostels/hostel_delete.html', {'hostel': hostel})
