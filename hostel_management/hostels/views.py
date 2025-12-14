from django.shortcuts import render, redirect
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
