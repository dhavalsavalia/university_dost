from django.shortcuts import render
from universities.models import University, Subject, Course
from .models import Exam, Question

def write_answers(request):
    return render(request, 'exams/index.html', {})
