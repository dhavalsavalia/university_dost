from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from exams.models import Question


@login_required
def write_answer(request):
    """This function handles answers!!!"""

    if request.method == 'POST':
        qpk = request.POST.get('qpk')
        question = Question.objects.get(pk=qpk)
        context = {
            'question': question
        }
        return render(request, 'exams/write_answer.html', context)
    else:
        return HttpResponse(status=403)
