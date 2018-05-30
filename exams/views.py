from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Exam, Question
from university.models import University, Course, Subject
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
