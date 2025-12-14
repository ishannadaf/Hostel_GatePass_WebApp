from django.shortcuts import render
from students.models import Student
from .models import GateIn
from django.utils import timezone
from accounts.decorators import role_required

@role_required('watchman', 'admin')
def gatein_entry(request):
    context = {}

    if request.method == 'POST':
        roll_no = request.POST['roll_no']

        try:
            student = Student.objects.get(roll_no=roll_no)

            today = timezone.now().date()
            already_in = GateIn.objects.filter(student=student, date=today).exists()

            if already_in:
                context['error'] = 'Student already marked Gate In today'
            else:
                GateIn.objects.create(
                    student=student,
                    watchman=request.user
                )
                context['success'] = f'Gate In marked for {student.name}'

        except Student.DoesNotExist:
            context['error'] = 'Student not found'

    return render(request, 'gatein/gatein.html', context)


@role_required('admin')
def gatein_list(request):
    records = GateIn.objects.all().order_by('-in_time')
    return render(request, 'gatein/gatein_list.html', {'records': records})
