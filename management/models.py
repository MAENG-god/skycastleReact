from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    studentName = models.CharField(max_length=20)
    studentGrade = models.CharField(max_length=50)
    
class StudyProgress(models.Model):
    studyProgress = models.TextField()
    studyDate = models.DateField()

class Homework(models.Model):
    homework = models.TextField()
    homeworkDate = models.DateField()

class Wage(models.Model):
    wageWay = models.CharField(max_length=10)
    wagePrice = models.IntegerField()