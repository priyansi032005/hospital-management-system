# prescriptions/models.py
from django.db import models
from django.conf import settings
from appointments.models import Appointment
from doctors.models import Doctor
from patients.models import Patient

User = settings.AUTH_USER_MODEL


class Prescription(models.Model):
    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name="prescription"
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="doctor_prescriptions"
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="patient_prescriptions"
    )

    medicines = models.TextField()
    instructions = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Prescription for {self.patient}"
