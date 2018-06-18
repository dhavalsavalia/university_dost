from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from exams.models import Question
from exams.forms import AnswerForm


@login_required
def write_answer(request):
    """This function handles answers!!!"""

    if request.method == 'POST':
        qpk = request.POST.get('qpk')
        question = Question.objects.get(pk=qpk)
        context = {
            'question': question,
            'form': AnswerForm
        }
        return render(request, 'exams/write_answer.html', context)
    else:
        return HttpResponse(status=403)
