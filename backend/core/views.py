from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings
import requests

BASE_URL = getattr(settings, "BASE_URL", "https://hospital-management-system-23.onrender.com")

API_LOGIN_URL = f"{BASE_URL}/api/login/"
API_REGISTER_URL = f"{BASE_URL}/api/register/"


def home(request):
    return JsonResponse({"status": "API running successfully"})


def login_page(request):
    if request.method == "POST":
        payload = {
            "username": request.POST.get("username"),
            "password": request.POST.get("password"),
        }

        try:
            response = requests.post(API_LOGIN_URL, json=payload, timeout=5)
        except requests.exceptions.RequestException as e:
            return render(request, "login.html", {
                "error": "Server error. Please try again later."
            })
        print(response.json())
        if response.status_code == 200:
            data = response.json()

            request.session["access"] = data.get("access")
            request.session["refresh"] = data.get("refresh")
            request.session["role"] = data.get("role")

            role = data.get("role")

            if role == "DOCTOR":
                return redirect("/doctor/dashboard/")
            elif role == "PATIENT":
                return redirect("/patient/dashboard/")
            else:
                return redirect("/admin/")

        return render(request, "login.html", {
            "error": "Invalid credentials"
        })

    return render(request, "login.html")


def register_page(request):
    if request.method == "POST":
        payload = {
            "username": request.POST.get("username"),
            "password": request.POST.get("password"),
            "role": request.POST.get("role"),
        }

        try:
            response = requests.post(API_REGISTER_URL, json=payload, timeout=5)
        except requests.exceptions.RequestException:
            return render(request, "register.html", {
                "error": "Server error. Please try again later."
            })

        if response.status_code == 201:
            return redirect("/login/")

        return render(request, "register.html", {
            "error": "Registration failed"
        })

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

