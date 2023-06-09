from django.db import models
from django.contrib.postgres.fields import ArrayField
# from django.apps import apps
from administrator.models import Student,ProgramReg,CourseRegitration


# class CourseRegitration(models.Model):
#     courseName=models.CharField(max_length=255)
#     code =models.CharField(max_length=200)
#     caMarks=models.CharField(max_length=200)
#     finalMarks=models.CharField(max_length=200)

#     def __str__(self):
#         return self.courseName
    
class Result(models.Model):
    program =models.ForeignKey(ProgramReg,on_delete=models.CASCADE)
    studentDetails=models.ForeignKey(Student,on_delete =models.CASCADE)
    course =models.ForeignKey(CourseRegitration, on_delete= models.CASCADE)
    # ExamType =[
    #     ('Test One','Test One'),
    #     ('Test Two','Test Two'),
    #     ('Final Exam','Final Exam'),
    # ]
    resultTypes=models.CharField(max_length=200)
    marks =models.CharField(max_length=200)
    # claim=models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.studentDetails)
    

