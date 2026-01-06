from rest_framework import serializers
from .models import Prescription


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = [
            "id",
            "appointment",
            "doctor",
            "patient",
            "medicines",
            "instructions",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "doctor",
            "patient",
            "created_at",
            "updated_at",
        ]
