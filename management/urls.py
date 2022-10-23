from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.ManagementStudents.as_view(), name="management"),
]