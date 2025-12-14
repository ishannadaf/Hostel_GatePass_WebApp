from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from accounts.decorators import role_required
import pandas as pd
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

@role_required('admin')
def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST.get('name'),
            roll_no=request.POST.get('roll_no'),
            contact_no=request.POST.get('contact_no'),
            parent_contact=request.POST.get('parent_contact'),
            stream=request.POST.get('stream'),
            division=request.POST.get('division'),
            year=request.POST.get('year'),
            hostel_name=request.POST.get('hostel_name'),
            room_no=request.POST.get('room_no'),
            taluka=request.POST.get('taluka'),
            district=request.POST.get('district'),
            city=request.POST.get('city'),
            gender=request.POST.get('gender'),
            photo=request.FILES.get('photo')
        )
        return redirect('/students/')

    return render(request, 'students/add_student.html')



@role_required('admin')
def student_list(request):
    q = request.GET.get('q', '')

    students_qs = Student.objects.filter(
        Q(name__icontains=q) |
        Q(roll_no__icontains=q)
    ).order_by('name')

    paginator = Paginator(students_qs, 10)  # 10 students per page
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)

    return render(request, 'students/student_list.html', {
        'students': students,
        'q': q
    })


@role_required('admin')
def student_edit(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.name = request.POST.get('name', student.name)
        student.roll_no = request.POST.get('roll_no', student.roll_no)
        student.contact_no = request.POST.get('contact_no', student.contact_no)
        student.parent_contact = request.POST.get('parent_contact', student.parent_contact)

        student.stream = request.POST.get('stream', student.stream)
        student.division = request.POST.get('division', student.division)
        student.year = request.POST.get('year', student.year)

        student.hostel_name = request.POST.get('hostel_name', student.hostel_name)
        student.room_no = request.POST.get('room_no', student.room_no)

        student.taluka = request.POST.get('taluka', student.taluka)
        student.district = request.POST.get('district', student.district)
        student.city = request.POST.get('city', student.city)

        student.gender = request.POST.get('gender', student.gender)

        if request.FILES.get('photo'):
            student.photo = request.FILES.get('photo')

        student.save()
        return redirect('/students/')

    return render(request, 'students/student_edit.html', {
        'student': student
    })



@role_required('admin')
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('/students/')

    return render(request, 'students/student_delete.html', {
        'student': student
    })
    


@role_required('admin')
def student_import(request):
    if request.method == 'POST' and request.FILES.get('file'):
        df = pd.read_excel(request.FILES['file'])

        for _, row in df.iterrows():
            Student.objects.create(
                name=row['name'],
                roll_no=row['roll_no'],
                contact_no=row['contact_no'],
                parent_contact=row['parent_contact'],
                stream=row['stream'],
                division=row['division'],
                year=row['year'],
                hostel_name=row['hostel_name'],
                room_no=row['room_no'],
                taluka=row['taluka'],
                district=row['district'],
                city=row['city'],
                gender=row['gender']
            )

        messages.success(request, 'Students imported successfully')
        return redirect('/students/')

    return render(request, 'students/student_import.html')
