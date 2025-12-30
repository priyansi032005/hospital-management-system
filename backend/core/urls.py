from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    home,
    login_page,
    register_page,
    logout_page,
    doctor_dashboard,
    appointment_list,
    prescription_list,
    prescriptionPDF_view,
    doctor_sidebar,
    doctor_settings,
    doctor_patient_list,
    patient_appointment_list,
    appointment_schedular,
    patient_dashboard,
    patient_profile,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),
    path("login/", login_page, name="login"),
    path("register/", register_page, name="register"),
    path("logout/", logout_page, name="logout"),
    path("doctor/appointments/", appointment_list, name="appointment_list"),
    path("doctor/dashboard/", doctor_dashboard, name="doctor_dashboard"),
    path("doctor/prescriptions/", prescription_list, name="prescription_list"),
    path("doctor/prescriptions/<int:prescription_id>/pdf/", prescriptionPDF_view, name="prescription_pdf"),
    path("doctor/sidebar/", doctor_sidebar, name="doctor_sidebar"),
    path("doctor/settings/", doctor_settings, name="doctor_settings"),
    path("doctor/patientlist/", doctor_patient_list, name="doctor_patient_list"),

    path("patient/dashboard/", patient_dashboard, name="patient_dashboard"),
    path("patient/appointments/", patient_appointment_list, name="patient_appointment_list"),
    path("patient/appointments/add/", appointment_schedular, name="appointment_schedular"),
    path("patient/profile/", patient_profile, name="patient_profile"),


    path("api/", include("accounts.urls")),
    path("api/appointments/", include("appointments.urls")),
    path("api/doctors/", include("doctors.urls")),
    path("api/patient/", include("patients.urls")),
    path("api/prescriptions/", include("prescriptions.urls")),
    path("api/medical_files/", include("medical_files.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)