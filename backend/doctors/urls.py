from django.urls import path

from .views import(
    DoctorProfileCreateView,
    DoctorProfileView,
    DoctorAppointmentsView,
    UpdateAppointmentStatusView
)

urlpatterns = [
    path('doctor/profile/create/', DoctorProfileCreateView.as_view()),
    path('doctor/profile/', DoctorProfileView.as_view()),
    path('doctor/appointments/', DoctorAppointmentsView.as_view()),
    path('doctor/appointment/<int:pk>/status', UpdateAppointmentStatusView.as_view())
]