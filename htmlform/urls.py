"""
URL configuration for htmlform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_school/',create_school,name='create_school'),
    path('create_subject/',create_subject,name='create_subject'),
    path('create_student/',create_student,name='create_student'),
    path('reterving_sub/',reterving_sub,name='reterving_sub'),
    path('reterving_stu/',reterving_stu,name='reterving_stu'),
    path('checkbox_sub/',checkbox_sub,name='checkbox_sub'),
    path('checkbox_stu/',checkbox_stu,name='checkbox_stu'),
]
