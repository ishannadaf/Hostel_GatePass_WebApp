from django.shortcuts import render, redirect
from .models import Student
from accounts.decorators import role_required

@role_required('admin')
def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST['name'],
            roll_no=request.POST['roll_no'],
            contact_no=request.POST['contact_no'],
            parent_contact=request.POST['parent_contact'],
            stream=request.POST['stream'],
            division=request.POST['division'],
            year=request.POST['year'],
            hostel_name=request.POST['hostel_name'],
            room_no=request.POST['room_no'],
            taluka=request.POST['taluka'],
            district=request.POST['district'],
            city=request.POST['city'],
            gender=request.POST['gender'],
            photo=request.FILES.get('photo')
        )
        return redirect('student_list')

    return render(request, 'students/add_student.html')


@role_required('admin')
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})
