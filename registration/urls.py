from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student_registration, name='student_registration'),
    path('course/', views.course_creation, name='course_creation'),
    path('enroll/', views.enrollment, name='enrollment'),
]