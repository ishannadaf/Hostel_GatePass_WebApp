from django.db import models
from students.models import Student
from accounts.models import User

class GatePass(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    watchman = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    reason = models.TextField()
    out_time = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.date}"
