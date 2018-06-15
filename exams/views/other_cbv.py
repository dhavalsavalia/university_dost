from django.views.generic import DetailView, ListView, UpdateView, CreateView
from exams.models import Exam, Question
from exams.forms import ExamForm, QuestionForm


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

    def get_queryset(self):
        exam = Exam.objects.get(exam_code=self.request.GET.get('q'))
        return Question.objects.filter(exam=exam)


class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm


class QuestionDetailView(DetailView):
    model = Question


class QuestionUpdateView(UpdateView):
    model = Question
    form_class = QuestionForm
