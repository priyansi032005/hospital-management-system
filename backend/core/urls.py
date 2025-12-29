"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
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
)

urlpatterns = [
    path("", home, name="home"),
    path("login/", login_page, name="login"),
    path("register/", register_page, name="register"),
    path("logout/", logout_page, name="logout"),

    path("doctor/appointments/", appointment_list, name="appointment_list"),

    path("doctor/dashboard/", doctor_dashboard, name="doctor_dashboard"),
    path("doctor/prescriptions/", prescription_list, name="prescription_list"),
    path("doctor/prescriptions/<int:prescription_id>/pdf/", prescriptionPDF_view, name="prescription_pdf"),
    path("doctor/sidebar/", doctor_sidebar, name="doctor_sidebar"),
]