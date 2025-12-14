from django.db import models

class Hostel(models.Model):
    hostel_name = models.CharField(max_length=100, unique=True)
    total_rooms = models.IntegerField()
    warden_name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hostel_name
