from django.db import models
from django.apps import apps

# Create your models here.

class ProgramReg(models.Model):
    name =models.CharField(max_length=255)
    TYPE =[
        ('Bachelor Degree','Bachelor Degree'),
        ('DIPLOMA','DIPLOMA'),
    ]
    type =models.CharField(max_length=200,choices=TYPE)
    durations=models.CharField(max_length=200)
    semisterNo=models.CharField(max_length=200)

    def __str__(self):
        return self.type+ ' in  '+ self.name



class CourseRegitration(models.Model):
    programName=models.ForeignKey(ProgramReg,on_delete=models.CASCADE)
    courseName=models.CharField(max_length=255)
    code=models.CharField(max_length=200)
    caMarks=models.CharField(max_length=200)
    finalMarks=models.CharField(max_length=200)

    def __str__(self):
        return self.courseName
    
class Student(models.Model):
    firstName =models.CharField(max_length=255)
    lastName =models.CharField(max_length=200) 
    registrtionNo =models.CharField(max_length =255)
    program=models.ForeignKey(ProgramReg,on_delete=models.CASCADE)
    image =models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.firstName+" "+self.lastName
    
