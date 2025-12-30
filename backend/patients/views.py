from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Patient
from .serializers import (
    PatientSerializer,
    DoctorListSerializer,
    AppointmentSerializer
)
from .permissions import IsPatient
from doctors.models import Doctor
from appointments.models import Appointment


# class CreatePatientProfileView(generics.CreateAPIView):
#     serializer_class = PatientSerializer
#     permission_classes = [IsAuthenticated, IsPatient]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)



class PatientProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated, IsPatient]

    def get_object(self):
        patient, _ = Patient.objects.get_or_create(
            user=self.request.user
        )
        return patient


class DoctorListView(generics.ListAPIView):
    serializer_class = DoctorListSerializer
    permission_classes = [IsAuthenticated, IsPatient]

    def get_queryset(self):
        return Doctor.objects.filter(is_available=True)


class CreateAppointmentView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsPatient]

    def perform_create(self, serializer):
        serializer.save(
            patient=self.request.user,
            status="PENDING"
        )



class PatientAppointmentsView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsPatient]

    def get_queryset(self):
        return Appointment.objects.filter(
            patient=self.request.user
        )



class PatientAppointmentDetailView(generics.RetrieveAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsPatient]

    def get_queryset(self):
        return Appointment.objects.filter(
            patient=self.request.user
        )


class CancelAppointmentView(APIView):
    permission_classes = [IsAuthenticated, IsPatient]

    def patch(self, request, pk):
        try:
            appointment = Appointment.objects.get(
                pk=pk,
                patient=request.user
            )
            appointment.status = "CANCELLED"
            appointment.save()
            return Response(
                {"message": "Appointment cancelled"},
                status=status.HTTP_200_OK
            )
        except Appointment.DoesNotExist:
            return Response(
                {"error": "Appointment not found"},
                status=status.HTTP_404_NOT_FOUND
            )



class PatientDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsPatient]

    def get(self, request):
        appointments = Appointment.objects.filter(
            patient=request.user
        )

        return Response({
            "total_appointments": appointments.count(),
            "pending": appointments.filter(status="PENDING").count(),
            "approved": appointments.filter(status="APPROVED").count(),
            "cancelled": appointments.filter(status="CANCELLED").count(),
        })



