from rest_framework import serializers
from .models import StudentInfo, StudyProgress, Homework, Wage

class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = '__all__'