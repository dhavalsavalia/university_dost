from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from exams.models import Question, AnswerFeedback
from django.contrib import messages


# we need feedback, like everyone does
# and we listen to them or do we? (Vsauce)
@login_required
def answer_feedback(request, exam_id, question_id):
    if request.is_ajax():
        feedback = AnswerFeedback(
            user=request.user,
            question=Question.objects.get(id=question_id),
            user_email=request.user.email,
            feedback_type=request.POST.get('feedback_type'),
            feedback_title=request.POST.get('feedback_title'),
            feedback_body=request.POST.get('feedback_body'),
        )
        feedback.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=404)


@login_required
def answer_feedback_list(request):
    """This function displays list of all feedbacks"""

    if request.user.has_perm('exams.change_answerfeedback'):
        feedbacks = AnswerFeedback.objects.all()
        context = {
            'feedbacks': feedbacks
        }
        return render(request, 'exams/answerfeedback_list.html', context)
    else:
        return HttpResponse(status=403)


@login_required
def answer_feedback_detail(request, pk):
    """This function displays detail of a feedback"""

    if request.user.has_perm('exams.change_answerfeedback'):
        feedback = AnswerFeedback.objects.get(pk=pk)
        context = {
            'feedback': feedback
        }
        return render(request, 'exams/answerfeedback_detail.html', context)
    else:
        return HttpResponse(status=403)


@login_required
def answer_feedback_update(request, pk):
    """
    This function updates status of a feedback.
    The status fuction will be added soon.
    """

    if request.user.has_perm('exams.change_answerfeedback'):
        feedback = AnswerFeedback.objects.get(pk=pk)
        if request.method == 'POST':
            new_feedback_status = request.POST.get('feedback_status')
            feedback.feedback_status = new_feedback_status
            feedback.save()
            messages.success(
                request,
                'Feedback status has been updated successfully!'
                )
            context = {
                'feedback': feedback
            }
            return render(request, 'exams/answerfeedback_form.html', context)
        else:
            context = {
                'feedback': feedback
            }
            return render(request, 'exams/answerfeedback_form.html', context)
    else:
        return HttpResponse(status=403)
