from rest_framework.permissions import BasePermission
from doctors.models import Doctor

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        return Doctor.objects.filter(user=request.user).exists()
