from django.db import models
from appointments.models import Appointment
from django.conf import settings

User = settings.AUTH_USER_MODEL

class MedicalFile(models.Model):
    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.CASCADE,
        related_name="medical_files"
    )
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to="medical_files/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File for appointment {self.appointment.id}"