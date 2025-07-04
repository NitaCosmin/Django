from django.db import models
from django.utils.timezone import now

class PersonalInfo(models.Model):
    full_name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/')
    cv_file = models.FileField(upload_to='cv/', blank=True, null=True)

    def __str__(self):
        return self.full_name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"Mesaj de la {self.name} ({self.sent_at.strftime('%d-%m-%Y %H:%M')})"
