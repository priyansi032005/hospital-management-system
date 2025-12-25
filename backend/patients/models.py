from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Patient(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="patient_profile",
        default=None
    )
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, default="Unknown")
    phone = models.CharField(max_length=15, default="0000000000")

    def __str__(self):
        return self.user.username
