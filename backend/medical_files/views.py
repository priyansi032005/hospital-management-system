from rest_framework import generics, permissions
from .models import MedicalFile
from .serializers import MedicalFileSerializer
from doctors.permissions import IsDoctor
from patients.permissions import IsPatient
from appointments.models import Appointment

# 🔹 PATIENT: UPLOAD MEDICAL FILE
class UploadMedicalFileView(generics.CreateAPIView):
    serializer_class = MedicalFileSerializer
    permission_classes = [permissions.IsAuthenticated, IsPatient]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

# 🔹 PATIENT: VIEW OWN MEDICAL FILES
class PatientMedicalFileListView(generics.ListAPIView):
    serializer_class = MedicalFileSerializer
    permission_classes = [permissions.IsAuthenticated, IsPatient]

    def get_queryset(self):
        return MedicalFile.objects.filter(uploaded_by=self.request.user)

# 🔹 DOCTOR: VIEW FILES BY APPOINTMENT
class DoctorMedicalFilesView(generics.ListAPIView):
    serializer_class = MedicalFileSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]

    def get_queryset(self):
        appointment_id = self.kwargs['appointment_id']
        return MedicalFile.objects.filter(
            appointment__id=appointment_id,
            appointment__doctor__user=self.request.user
        )
