from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from exams.models import Exam, Question, AnswerFeedback
from universities.models import University, Course, Subject


@login_required
def view_answers(request):
    """Main entry-point to view answers"""
    if request.method == 'POST':
        context = {
            'university': University.objects.get(
                id=request.POST['university']
                ),
            'course': Course.objects.get(
                id=request.POST['course']
                ),
            'subject': Subject.objects.get(
                id=request.POST['subject']
                ),
            'exam': Exam.objects.get(
                id=request.POST['exam']
                ),
            'exam_questions': Question.objects.filter(
                exam=request.POST['exam']
                )
            .order_by('question_code'),
        }
        return render(request, 'exams/submit_result.html', context)
    else:
        universities = University.objects.all().values(
            'name', 'university_code', 'id').order_by('name')
        universities_list = list()
        for university in universities:
            universities_list.append(university)
        context = {'universities': universities_list}
    return render(request, 'exams/view_answer_select_exam.html', context)


@login_required
def view_question_paper(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    exam_questions = Question.objects.filter(
        exam_id=exam_id
        ).order_by('question_code')
    context = {
        'university': exam.subject.course.university,
        'course': exam.subject.course,
        'subject': exam.subject,
        'exam': exam,
        'exam_questions': exam_questions,
    }
    return render(request, 'exams/view_question_paper.html', context)


@login_required
def view_answer(request, exam_id, question_id):
    question = Question.objects.get(id=question_id)
    question_number = question.question_number

    # check whether the user has cased vote or not
    # all in one because, you know, memory, poor guy, me
    if (request.user.upvoted_questions.filter(id=question_id) or
            request.user.downvoted_questions.filter(id=question_id)):
        casted_vote = True
    else:
        casted_vote = False

    # calculate percentage and stuff like that
    # huge shoutout to Hemnag Vyas
    if question.downvote == 0 and question.upvote == 0:
        vote_msg = 'No one has voted, yet. Author is sad.'
    elif question.downvote == 0:
        vote_msg = 'Hooray! Everyone upvoted this answer'
    else:
        upvote_percentage = (
            question.upvote/(question.upvote+question.downvote)
            )*100
        vote_msg = '''{}% people find this answer helpful.
                    Was this answer helpful to you?'''.format(
                        upvote_percentage
                        )

    context = {
        'univquestionersity': question.exam.subject.course.university,
        'course': question.exam.subject.course,
        'subject': question.exam.subject,
        'exam': question.exam,
        'question': question,
        'casted_vote': casted_vote,
        'vote_msg': vote_msg,

        # Issue: whatever the hell it is, it breaks when author navigates.
        # I hope s/he doesn't need my website. Poor guys. :(
        # a litter hack to get previous question
        'prev_question': (Question.objects
                          .filter(exam=question.exam,
                                  question_number__lte=question_number,
                                  id__lt=question.id)
                          .exclude(id=question.id)
                          .order_by('-question_number',)
                          .first()),

        # another litter hack to get next question
        'next_question': (Question.objects
                          .filter(exam=question.exam,
                                  question_number__gte=question_number,
                                  id__gt=question.id)
                          .exclude(id=question.id)
                          .order_by('question_number')
                          .first())
    }
    return render(request, 'exams/view_answer.html', context)


# fate of an author is casted here
# the voting procedure
@login_required
def vote(request, exam_id, question_id):
    if request.is_ajax():
        question = Question.objects.get(id=question_id)

        # do i need to explain?
        # I am not THAT bad a programmer
        if request.POST.get('vote_type') == 'upvote':
            question.upvote += 1
            question.save()
            request.user.upvoted_questions.add(question)
            return JsonResponse({'result': 'upvote success'})

        elif request.POST.get('vote_type') == 'downvote':
            question.downvote += 1
            question.save()
            request.user.downvoted_questions.add(question)
            return JsonResponse({'result': 'downvote success'})

        else:
            return JsonResponse({'result': 'what the fuck?'})
    else:
        return HttpResponse(status=404)


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
