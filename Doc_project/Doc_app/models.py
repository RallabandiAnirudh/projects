from django.db import models

# Create your models here.
class Patient(models.Model):
    full_name = models.CharField(max_length=50)
    age = models.CharField(max_length=2)
    gender = models.CharField(max_length=7)
    phone_no = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    health_issue = models.CharField(max_length=200)
    available_timings = models.TimeField(auto_now=False, auto_now_add=False)


def __str__(self):
    return self.full_name
