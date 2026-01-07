from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Appointment
from .serializers import AppointmentSerializer


class AppointmentViewSet(ModelViewSet):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "DOCTOR":
            return Appointment.objects.filter(doctor__user=user)
        elif user.role == "PATIENT":
            return Appointment.objects.filter(patient__user=user)
        return Appointment.objects.none()
