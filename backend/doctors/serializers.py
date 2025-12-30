from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(
        source="user.username", read_only=True
    )
    email = serializers.EmailField(
        source="user.email", read_only=True
    )
    class Meta:
        model = Doctor
        fields = [
            "id",
            "full_name",
            "email",
            "phone",
            "specialization",
            "experience_years",
            "license_number",
            "bio",
            "hospital_name",
            "department",
            "office_address",
            "city",
            "is_available",
            "created_at",
        ]
        read_only_fields = ['user']
