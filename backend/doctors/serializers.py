from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Doctor
        fields = [
            "id",
            "username",
            "email",
            "specialization",
            "experience_years",
            "phone",
            "bio"
        ]
        read_only_fields = ["username", "email"]
