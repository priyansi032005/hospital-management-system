from rest_framework import generics, permissions
from .models import Prescription
from .serializers import PrescriptionSerializer
from doctors.permissions import IsDoctor
from patients.permissions import IsPatient
from appointments.models import Appointment

# 🔹 DOCTOR: CREATE PRESCRIPTION
class CreatePrescriptionView(generics.CreateAPIView):
    serializer_class = PrescriptionSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]

    def perform_create(self, serializer):
        appointment = Appointment.objects.get(
            id=self.request.data.get("appointment")
        )
        serializer.save(
            doctor=self.request.user,
            patient=appointment.patient
        )

# 🔹 DOCTOR: VIEW HIS PRESCRIPTIONS
class DoctorPrescriptionListView(generics.ListAPIView):
    serializer_class = PrescriptionSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]

    def get_queryset(self):
        return Prescription.objects.filter(doctor=self.request.user)

# 🔹 PATIENT: VIEW PRESCRIPTIONS
class PatientPrescriptionListView(generics.ListAPIView):
    serializer_class = PrescriptionSerializer
    permission_classes = [permissions.IsAuthenticated, IsPatient]

    def get_queryset(self):
        return Prescription.objects.filter(patient=self.request.user)

