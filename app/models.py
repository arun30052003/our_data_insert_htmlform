from django.db import models

# Create your models here.

class School(models.Model):
    School_Name=models.CharField(max_length=100,primary_key=True)
    School_Location=models.CharField(max_length=100)
    Principal_Name=models.CharField(max_length=100)

    def __str__(self):
        return self.School_Name
    

class Subject(models.Model):
    School_Name=models.ForeignKey(School,on_delete=models.CASCADE)
    Subject_Name=models.CharField(max_length=100)
    Teacher_Name=models.CharField(max_length=100)

    def __str__(self):
        return self.Subject_Name
    

class Student(models.Model):
    Subject_Name=models.ForeignKey(Subject,on_delete=models.CASCADE)
    Student_Id=models.IntegerField()
    Student_Name=models.CharField(max_length=100)

    def __str__(self):
        return str(self.Student_Id)