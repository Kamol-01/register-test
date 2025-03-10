from django.shortcuts import render, redirect
from .forms import StudentForm, CourseForm, EnrollmentForm
from .models import Student, Course, Enrollment

def student_registration(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_registration')
    else:
        form = StudentForm()
    return render(request, 'registration/student_registration.html', {'form': form})

def course_creation(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_creation')
    else:
        form = CourseForm()
    return render(request, 'registration/course_creation.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import EnrollmentForm

def enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollment')  # เปลี่ยนเส้นทางหลังจากบันทึกข้อมูล
    else:
        form = EnrollmentForm()
    return render(request, 'registration/enrollment.html', {'form': form})