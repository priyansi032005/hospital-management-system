from rest_framework import serializers
from .models import MedicalFile


class MedicalFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalFile
        fields = '__all__'
        read_only_fields = ['patient', 'doctor']
