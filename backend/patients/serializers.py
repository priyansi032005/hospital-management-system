from rest_framework import serializers
from .models import Patient
from doctors.models import Doctor
from appointments.models import Appointment

class PatientSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="user.username", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Patient
        fields = [
            "id",
            "name",
            "email",
            "age",
            "gender",
            "phone",
            "address",
            "blood_group",
            "health_status",
            "allergies",
            "chronic_conditions",
            "current_medications",
            "family_medical_history",
            "insurance_provider",
            "insurance_policy_number",
            "emergency_contact_name",
            "emergency_contact_phone",
            "created_at",
        ]
        read_only_fields = ["user"]


class DoctorListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")

    class Meta:
        model = Doctor
        fields = [
            "id",
            "username",
            "specialization",
            "experience_years",
            "phone",
            "is_available"
        ]


class AppointmentSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(
        source="doctor.user.username",
        read_only=True
    )

    class Meta:
        model = Appointment
        fields = [
            "id",
            "appointment_date",
            "status",
            "doctor",
            "doctor_name"
        ]
        read_only_fields = ["status"]
