from django.shortcuts import render

# Create your views here.
from app.models import *

def create_school(request):
    if request.method=='POST':
        School_Name=request.POST['sn']
        School_Location=request.POST['sl']
        Principal_Name=request.POST['pn']

        SO=School.objects.get_or_create(School_Name=School_Name,School_Location=School_Location,Principal_Name=Principal_Name)[0]
        SO.save()

        ST=School.objects.all()
        d={'datas':ST}
        return render(request,'school_data.html',d)
    return render(request,'create_school.html')



def create_subject(request):
    ST=School.objects.all()
    d={'datas':ST}
    if request.method=='POST':
        School_Name=request.POST['sn']
        Subject_Name=request.POST['sun']
        Teacher_Name=request.POST['tn']

        SO=School.objects.get(School_Name=School_Name)
        SUBO=Subject.objects.get_or_create(School_Name=SO,Subject_Name=Subject_Name,Teacher_Name=Teacher_Name)[0]
        SUBO.save()

        SUT=Subject.objects.all()
        d={'datas':SUT}
        return render(request,'subject_data.html',d)
    return render(request,'create_subject.html',d)



def create_student(request):
    SUT=Subject.objects.all()
    d={'datas':SUT}
    if request.method=='POST':
        pk=request.POST['sun']
        Student_Id=request.POST['si']
        Student_Name=request.POST['sn']

        SO=Subject.objects.get(pk=pk)
        STO=Student.objects.get_or_create(Subject_Name=SO,Student_Id=Student_Id,Student_Name=Student_Name)[0]
        STO.save()

        STT=Student.objects.all()
        d={'datas':STT}
        return render(request,'student_data.html',d)
    return render(request,'create_student.html',d)