"""health_care_live_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from health_care_live_project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage),
    path('about-us',views.aboutPage),
    path('service',views.servicePage),
    path('contact-us',views.contactPage),
    path('all-doctor/<int:id>',views.allDoctorPage),
    path('single-doctor/<int:id>',views.singleDoctorDetails),
    path('appointment/<int:id>',views.appointmentPage),
    path('get-doctor-department-name-ajax/', views.get_doctor_department_name_ajax,name="get_doctor_department_name_ajax"),
]
