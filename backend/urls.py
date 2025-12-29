from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("backend.urls")),
    path("api/", include("accounts.urls")),
    path("api/appointments/", include("appointments.urls")),
    path("api/doctors/", include("doctors.urls")),
    path("api/patient/", include("patients.urls")),
    path("api/prescriptions/", include("prescriptions.urls")),
    path("api/medical_files/", include("medical_files.urls")),
]
