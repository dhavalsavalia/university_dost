from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from exams.models import Question
from exams.forms import AnswerForm


@login_required
def write_answer(request, exam_pk, question_pk):
    """This function handles answers!!!"""

    if request.user.has_perm('exams.change_question'):
        question = Question.objects.get(pk=question_pk)
        context = {
            'question': question,
            'form': AnswerForm
        }
        return render(request, 'exams/write_answer.html', context)
    else:
        return HttpResponse(status=403)
