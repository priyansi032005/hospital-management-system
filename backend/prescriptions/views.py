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

        try:
            doctor = Doctor.objects.get(user=appointment.doctor.user)
            patient = Patient.objects.get(user=appointment.patient.user)
        except (Doctor.DoesNotExist, Patient.DoesNotExist):
            raise ValidationError("Doctor or Patient profile not found")

        serializer.save(
            doctor=doctor,
            patient=patient
        )


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

