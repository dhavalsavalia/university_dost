from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseServerError
from .models import Exam, Question
from universities.models import University, Course, Subject
from .forms import ExamForm, QuestionForm


class ExamListView(ListView):
    model = Exam


class ExamCreateView(CreateView):
    model = Exam
    form_class = ExamForm


class ExamDetailView(DetailView):
    model = Exam


class ExamUpdateView(UpdateView):
    model = Exam
    form_class = ExamForm


class QuestionListView(ListView):
    model = Question


class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm


class QuestionDetailView(DetailView):
    model = Question


class QuestionUpdateView(UpdateView):
    model = Question
    form_class = QuestionForm


def write_answers(request):
    """Main entry-point to start writing answers"""
    if request.method == 'POST':
        context = {
            'university': University.objects.get(id=request.POST['university']),
            'course': Course.objects.get(id=request.POST['course']),
            'subject': Subject.objects.get(id=request.POST['subject']),
            'exam': Exam.objects.get(id=request.POST['exam']),
        }
        return render(request, 'exams/submit_result.html', context)
    else:
        universities = University.objects.all().values(
            'name', 'university_code', 'id').order_by('name')
        universities_list = list()
        for university in universities:
            universities_list.append(university)
    return render(request, 'exams/write_answers.html', {'universities': universities_list})


def get_courses(request):
    """Handler to return JsonResponse of available courses"""

    if request.is_ajax():
        university_id = request.GET.get('ui')
        if Course.objects.filter(university_id=university_id).exists():
            courses = Course.objects.filter(
                university_id=university_id).values('id', 'name')
        else:
            return JsonResponse({'no_result': True})
        courses_list = list()
        for course in courses:
            courses_list.append(course)
        return JsonResponse(courses_list, safe=False)
    else:
        return HttpResponseServerError()


def get_subjects(request):
    """Handler to return JsonResponse of available subjects"""

    if request.is_ajax():
        course_id = request.GET.get('ci')
        if Subject.objects.filter(course_id=course_id).exists():
            subjects = Subject.objects.filter(
                course_id=course_id).values('id', 'name')
        else:
            return JsonResponse({'no_result': True})
        subjects_list = list()
        for subject in subjects:
            subjects_list.append(subject)
        return JsonResponse(subjects_list, safe=False)
    else:
        return HttpResponseServerError()


def get_exams(request):
    """Handler to return JsonResponse of available exams"""
    if request.is_ajax():
        subject_id = request.GET.get('si')
        if Exam.objects.filter(subject_id=subject_id).exists():
            exams = Exam.objects.filter(
                subject_id=subject_id).values('id', 'month', 'year')
        else:
            return JsonResponse({'no_result': True})
        exam_list = list()
        for exam in exams:
            exam_list.append(exam)
        return JsonResponse(exam_list, safe=False)
    else:
        return HttpResponseServerError()
