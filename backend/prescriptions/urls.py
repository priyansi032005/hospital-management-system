from django.urls import path
from .views import (
    CreatePrescriptionView,
    DoctorPrescriptionListView,
    PatientPrescriptionListView
)

urlpatterns = [
    path('doctor/create/', CreatePrescriptionView.as_view()),
    path('doctor/', DoctorPrescriptionListView.as_view()),
    path('patient/', PatientPrescriptionListView.as_view()),
]
