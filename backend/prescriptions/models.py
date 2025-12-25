from django.db import models
from appointments.models import Appointment
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Prescription(models.Model):
    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.CASCADE,
        related_name="prescriptions"
    )
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="patient_prescriptions"
    )
    medicines = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient}"