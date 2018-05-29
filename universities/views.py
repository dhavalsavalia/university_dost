from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import University, Course, Subject
from .forms import UniversityForm, CourseForm, SubjectForm


class UniversityListView(ListView):
    model = University


class UniversityCreateView(CreateView):
    model = University
    form_class = UniversityForm


class UniversityDetailView(DetailView):
    model = University


class UniversityUpdateView(UpdateView):
    model = University
    form_class = UniversityForm


class CourseListView(ListView):
    model = Course


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm


class CourseDetailView(DetailView):
    model = Course


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm


class SubjectListView(ListView):
    model = Subject


class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm


class SubjectDetailView(DetailView):
    model = Subject


class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm
