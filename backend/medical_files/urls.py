from django.urls import path
from .views import (
    UploadMedicalFileView,
    PatientMedicalFileListView,
    DoctorMedicalFilesView
)

urlpatterns = [
    path('patient/', PatientMedicalFileListView.as_view()),
    path('patient/upload/', UploadMedicalFileView.as_view()),
    path('doctor/<int:appointment_id>/', DoctorMedicalFilesView.as_view()),
]
