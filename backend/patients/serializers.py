from rest_framework import serializers
from .models import Patient
from doctors.models import Doctor
from appointments.models import Appointment

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
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
