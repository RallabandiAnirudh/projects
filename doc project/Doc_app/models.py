from django.db import models

# Create your models here.
class Clinic(models.Model):
    Doctor_name = models.CharField(max_length=50)
    Specialization = models.CharField(max_length=50)
    Description = models.TextField(default="")
    Available_timings = models.TimeField(auto_now=False, auto_now_add=False)


def __str__(self):
    return self.Doctor_name

