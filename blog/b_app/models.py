from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.CharField(max_length=100)
    image = models.ImageField(null=True,blank=True, upload_to="images/")
    likes = models.ManyToManyField(User, related_name='profile', blank=True)
    caption = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user

