from django.db import models
from django.utils import timezone

class Appointment(models.Model):
    APPOINTMENT_TYPE_CHOICES = [
        ("ONLINE", "Online Appointment"),
        ("OFFLINE", "Offline Appointment"),
    ]

    patient = models.ForeignKey(
        "patients.Patient",
        on_delete=models.CASCADE
    )
    doctor = models.ForeignKey(
        "doctors.Doctor",
        on_delete=models.CASCADE
    )

    specialty = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    patient_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    phone_number = models.CharField(
        max_length=15,
        null=True,
        blank=True
    )

    appointment_date = models.DateField()

    time_slot = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    appointment_type = models.CharField(
        max_length=10,
        choices=APPOINTMENT_TYPE_CHOICES,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        default="PENDING"
    )

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.patient_name} - {self.doctor}"
