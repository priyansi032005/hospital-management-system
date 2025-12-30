from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Doctor
from .serializers import DoctorSerializer
from .permissions import IsDoctor

from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer


class DoctorProfileCreateView(generics.CreateAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if Doctor.objects.filter(user=self.request.user).exists():
            raise ValidationError("Doctor profile already exists.")
        serializer.save(user=self.request.user)


class DoctorProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]

    def get_object(self):
        return Doctor.objects.get(user=self.request.user)


class DoctorAppointmentsView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]

    def get_queryset(self):
        return Appointment.objects.filter(
            doctor__user=self.request.user
        )


class UpdateAppointmentStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsDoctor]

    def patch(self, request, pk):
        try:
            appointment = Appointment.objects.get(
                pk=pk,
                doctor__user=request.user
            )
            appointment.status = request.data.get("status")
            appointment.save()

            return Response(
                {"message": "Appointment status updated"},
                status=status.HTTP_200_OK
            )

        except Appointment.DoesNotExist:
            return Response(
                {"error": "Appointment not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class DoctorDashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsDoctor]

    def get(self, request):
        appointments = Appointment.objects.filter(
            doctor__user=request.user
        )

        return Response({
            "total_appointments": appointments.count(),
            "pending": appointments.filter(status="PENDING").count(),
            "approved": appointments.filter(status="APPROVED").count(),
            "cancelled": appointments.filter(status="CANCELLED").count(),
        })