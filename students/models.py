from django.db import models

class Student(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=50, unique=True)
    contact_no = models.CharField(max_length=15)
    parent_contact = models.CharField(max_length=15)
    stream = models.CharField(max_length=100)
    division = models.CharField(max_length=10)
    year = models.CharField(max_length=20)
    hostel_name = models.CharField(max_length=100)
    room_no = models.CharField(max_length=10)
    taluka = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    photo = models.ImageField(upload_to='students/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
