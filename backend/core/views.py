from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings
import requests
from django.contrib.auth import login
from accounts.models import User


BASE_URL = getattr(settings, "BASE_URL", "http://127.0.0.1:8000")

API_LOGIN_URL = f"{BASE_URL}/api/login/"
API_REGISTER_URL = f"{BASE_URL}/api/register/"


def home(request):
    return JsonResponse({"status": "API running successfully"})


def login_page(request):
    return render(request, "login.html")


def register_page(request):
    return render(request, "register.html")


def logout_page(request):
    request.session.flush()
    return redirect("/login/")


def doctor_dashboard(request):
    return render(request, "Doctor/DoctorDash/DoctorMain.html")

def appointment_list(request):
    return render(request, "Doctor/DoctorAppointment/appointment_list.html")

def prescription_list(request):
    return render(request, "Doctor/DoctorDash/PrescriptionModule.html")

def prescriptionPDF_view(request, prescription_id):
    return render(request, "Doctor/DoctorDash/PrescriptionPDF.html", {
        "prescription_id": prescription_id
    })

def doctor_sidebar(request):
    return render(request, "Doctor/DoctorSidebar/DoctorSidebar.html")

def doctor_settings(request):
    return render(request, "Doctor/DoctorSettings/DoctorSettings.html")

def doctor_patient_list(request):
    return render(request, "Doctor/DoctorPatientList.html")

def patient_dashboard(request):
    return render(request, "Patient/PatientDash/PatientDash.html")

def patient_appointment_list(request):
    return render(request, "Patient/PatientAppointment/PatientAppointmentList.html")

def appointment_schedular(request):
    return render(request, "Patient/PatientAppointment/AppointmentSchedular.html")

def patient_profile(request):
    return render(request, "Patient/PatientProfile/PatientProfile.html")
