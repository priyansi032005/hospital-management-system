from django.db import models
from django.conf import settings


class Doctor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='doctor_profile'
    )
    specialization = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()
    phone = models.CharField(max_length=15)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
