from django.contrib import admin
from .models import CourseRegitration,ExaminationResults

# Register your models here.

class CourseReg(admin.ModelAdmin):
       list_display = ('courseName','code','caMarks','finalMarks')
       
admin.site.register(CourseRegitration,CourseReg)


class ExaminationAdmin(admin.ModelAdmin):
       list_display = ('studentDetails', 'course','examTypes','marks')
admin.site.register(ExaminationResults,ExaminationAdmin)
