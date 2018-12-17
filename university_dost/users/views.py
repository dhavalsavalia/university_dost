from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from exams.models import Exam, Question
from exams.forms import AnswerForm
from .models import User
from django.contrib.auth.decorators import login_required
from universities.models import University, Course, Subject
from django.http import HttpResponse


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ["first_name", "last_name", "university",
              "semester", "weekly_test"
              ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update

    def get_success_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


@login_required
def question_list(request):
    """Main entry-point to start writing answers"""

    if request.user.has_perm('exams.change_question'):
        # Check whether user is in "answers_wizard" group
        if request.method == 'POST':
            context = {
                'university': University.objects.get(
                                                id=request.POST['university']
                                                ),
                'course': Course.objects.get(id=request.POST['course']),
                'subject': Subject.objects.get(id=request.POST['subject']),
                'exam': Exam.objects.get(id=request.POST['exam']),
                'exam_questions': request.user.questions.filter(
                                                exam__id=request.POST['exam']
                                                )
                .order_by('question_code'),
            }
            return render(request, 'users/question_list.html', context)
        else:
            universities = University.objects.all().values(
                'name', 'university_code', 'id').order_by('name')
            universities_list = list()
            for university in universities:
                universities_list.append(university)
            context = {'universities': universities_list}
        return render(request, 'exams/write_answers.html', context)
    else:
        return HttpResponse(status=403)


@login_required
def update_answer(request, qpk):
    """This function handles answers!!!"""

    if request.user.has_perm('exams.change_question'):
        question = Question.objects.get(pk=qpk)
        context = {
            'question': question,
            'form': AnswerForm
        }
        return render(request, 'exams/write_answer.html', context)
    else:
        return HttpResponse(status=403)
