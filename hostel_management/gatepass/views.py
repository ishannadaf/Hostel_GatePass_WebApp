from django.shortcuts import render
from students.models import Student
from gatein.models import GateIn
from .models import GatePass
from django.utils import timezone
from accounts.decorators import role_required
from .sms_service import send_sms
from accounts.utils import log_activity


@role_required('watchman', 'admin')
def gatepass_entry(request):
    context = {}

    if request.method == 'POST':
        roll_no = request.POST['roll_no']
        reason = request.POST['reason']

        try:
            student = Student.objects.get(roll_no=roll_no)
            today = timezone.now().date()

            gate_in_exists = GateIn.objects.filter(student=student, date=today).exists()
            gate_pass_exists = GatePass.objects.filter(student=student, date=today).exists()

            if not gate_in_exists:
                context['error'] = 'Student has not entered today'

            elif gate_pass_exists:
                context['error'] = 'Gate Pass already issued today'

            else:
                GatePass.objects.create(
                    student=student,
                    watchman=request.user,
                    reason=reason
                )
                log_activity(request.user, f"Gate Pass - Student {student.name} ({student.roll_no})")

                # ===== SMS LOGIC =====
                parent_mobile = student.parent_contact

                name1 = student.name
                n2 = ""
                
                sms_status = send_sms(parent_mobile, name1, n2)

                if sms_status:
                    context['success'] = f"Gate Pass issued & SMS sent to parent"
                else:
                    context['success'] = f"Gate Pass issued (SMS failed)"

        except Student.DoesNotExist:
            context['error'] = 'Student not found'

    return render(request, 'gatepass/gatepass.html', context)


@role_required('admin')
def gatepass_list(request):
    records = GatePass.objects.all().order_by('-out_time')
    return render(request, 'gatepass/gatepass_list.html', {'records': records})
