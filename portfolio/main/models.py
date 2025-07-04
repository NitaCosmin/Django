from django.db import models
from django.utils.timezone import now


cv_file = models.FileField(upload_to='cv/', null=True, blank=True)

from django.contrib.auth.models import User

class PersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # legătură cu utilizatorul
    full_name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    cv_file = models.FileField(upload_to='cv/', null=True, blank=True)

    def __str__(self):
        return self.full_name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.name} - {self.sent_at.strftime('%d-%m-%Y %H:%M')}"
