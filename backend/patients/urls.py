from django.urls import path
from .views import *

urlpatterns = [
    # path("profile/create/", CreatePatientProfileView.as_view()),
    path("profile/", PatientProfileView.as_view()),

    path("doctors/", DoctorListView.as_view()),

    path("appointments/create/", CreateAppointmentView.as_view()),
    path("appointments/", PatientAppointmentsView.as_view()),
    path("appointment/<int:pk>/", PatientAppointmentDetailView.as_view()),
    path("appointment/<int:pk>/cancel/", CancelAppointmentView.as_view()),

    path("dashboard/", PatientDashboardView.as_view()),
]
