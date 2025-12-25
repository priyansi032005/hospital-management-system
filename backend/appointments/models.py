from django.db import models
from django.conf import settings
from doctors.models import Doctor

User = settings.AUTH_USER_MODEL

class Appointment(models.Model):
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="patient_appointments"
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="doctor_appointments",
        null=True,
        blank=True
    )
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20, default="PENDING")

    def __str__(self):
        return f"{self.patient} -> {self.doctor}"
