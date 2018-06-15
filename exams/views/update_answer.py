from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from exams.models import Question


@login_required
def update_answer(request):
    """This function updates/adds answer"""

    if request.method == 'POST':
        question = Question.objects.get(pk=request.POST.get('qpk'))
        question.answer = request.POST.get('answer')
        question.explanation = request.POST.get('explanation')
        question.author = request.user
        question.save()
        context = {
            'author': request.user,
            'question': question
        }
        return render(request, 'exams/success.html', context)
    else:
        return HttpResponse(status=403)
