# prescriptions/views.py
from rest_framework import generics, permissions
from .models import Prescription
from .serializers import PrescriptionSerializer
from doctors.permissions import IsDoctor
from appointments.models import Appointment
from doctors.models import Doctor
from patients.models import Patient
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

class CreatePrescriptionView(generics.CreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated, IsDoctor]

    def perform_create(self, serializer):
        appointment = serializer.validated_data["appointment"]

        if appointment.doctor.user != self.request.user:
            raise ValidationError("You are not allowed to create a prescription for this appointment")

        if hasattr(appointment, "prescription"):
            raise ValidationError("Prescription already exists for this appointment")

        serializer.save()



# 🔹 DOCTOR: VIEW HIS PRESCRIPTIONS
class DoctorPrescriptionListView(generics.ListAPIView):
    serializer_class = PrescriptionSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]

    def get_queryset(self):
        return Prescription.objects.filter(doctor__user=self.request.user)

# 🔹 PATIENT: VIEW PRESCRIPTIONS
class PatientPrescriptionListView(generics.ListAPIView):
    serializer_class = PrescriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Prescription.objects.filter(patient__user=self.request.user)

