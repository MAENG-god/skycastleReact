from django.shortcuts import render
from rest_framework import generics
from .models import StudentInfo, StudyProgress, Homework, Wage
from .serializers import StudentInfoSerializer

# Create your views here.

class ManagementStudents(generics.ListAPIView):
    queryset = StudentInfo.objects.all()
    serializer_class = StudentInfoSerializer