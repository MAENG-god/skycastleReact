from django.contrib import admin
from .models import StudentInfo, StudyProgress, Homework, Wage

# Register your models here.

admin.site.register(StudentInfo)
admin.site.register(StudyProgress)
admin.site.register(Homework)
admin.site.register(Wage)

