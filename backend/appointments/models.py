from django.db import models

class Appointment(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, default='PENDING')

    def __str__(self):
        return f"{self.patient} → {self.doctor}"