from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Patient(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="patient_profile"
    )

    # Basic Info
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True, null=True)

    # Health Summary
    blood_group = models.CharField(max_length=5, blank=True)
    health_status = models.CharField(max_length=50, blank=True)

    # Medical Details
    allergies = models.TextField(blank=True)
    chronic_conditions = models.TextField(blank=True)
    current_medications = models.TextField(blank=True)
    family_medical_history = models.TextField(blank=True)

    # Insurance & Emergency
    insurance_provider = models.CharField(max_length=100, blank=True)
    insurance_policy_number = models.CharField(max_length=50, blank=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
