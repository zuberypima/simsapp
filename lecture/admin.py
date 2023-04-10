from django.contrib import admin
from .models import Result

# Register your models here.

# class CourseReg(admin.ModelAdmin):
#        list_display = ('courseName','code','caMarks','finalMarks')
       
# admin.site.register(CourseRegitration,CourseReg)


class ExaminationAdmin(admin.ModelAdmin):
       list_display = ('studentDetails', 'course','resultTypes','marks')
admin.site.register(Result,ExaminationAdmin)
