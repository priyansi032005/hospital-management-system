from django.urls import path
from .views import (
    DoctorProfileCreateView,
    DoctorProfileView,
    DoctorAppointmentsView,
    UpdateAppointmentStatusView,
    DoctorDashboardView
)

urlpatterns = [
    path('profile/create/', DoctorProfileCreateView.as_view()),
    path('profile/', DoctorProfileView.as_view()),
    path('appointments/', DoctorAppointmentsView.as_view()),
    path('appointment/<int:pk>/status/', UpdateAppointmentStatusView.as_view()),
    path("dashboard/", DoctorDashboardView.as_view()),
]