from rest_framework import serializers
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(
        source="doctor.user.username",
        read_only=True
    )

    patient_name = serializers.CharField(
        source="patient.user.username",
        read_only=True
    )

    patient_email = serializers.EmailField(
        source="patient.user.email",
        read_only=True
    )

    phone_number = serializers.CharField(
        source="patient.phone_number",
        read_only=True
    )

    class Meta:
        model = Appointment
        fields = [
            "id",
            "appointment_date",
            "time_slot",
            "appointment_type",
            "status",
            "patient",
            "patient_name",
            "patient_email",
            "phone_number",
            "doctor",
            "doctor_name",
        ]
        read_only_fields = ["status"]
