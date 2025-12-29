from django.http import JsonResponse
from django.shortcuts import render, redirect
import requests

API_LOGIN_URL = "http://127.0.0.1:8000/api/login/"
API_REGISTER_URL = "http://127.0.0.1:8000/api/register/"


def home(request):
    return JsonResponse({"status": "API running successfully"})


def login_page(request):
    if request.method == "POST":
        payload = {
            "username": request.POST.get("username"),
            "password": request.POST.get("password"),
        }

        response = requests.post(API_LOGIN_URL, json=payload)

        if response.status_code == 200:
            data = response.json()

            request.session["access"] = data.get("access")
            request.session["refresh"] = data.get("refresh")

            return redirect("/patient/dashboard/")
        else:
            return render(request, "login.html", {
                "error": "Invalid credentials"
            })
    return render(request, "login.html")


def register_page(request):
    if request.method == "POST":
        payload = {
            "username": request.POST.get("username"),
            "email": request.POST.get("email"),
            "password": request.POST.get("password"),
        }

        response = requests.post(API_REGISTER_URL, json=payload)

        if response.status_code == 201:
            return redirect("/login/")
        else:
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

def patient_appointment_list(request):
    return render(request, "Patient/PatientAppointment/PatientAppointmentList.html")