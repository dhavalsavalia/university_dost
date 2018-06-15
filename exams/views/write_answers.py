from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from exams.models import Exam, Question
from universities.models import University, Course, Subject


@login_required
def write_answers(request):
    """Main entry-point to start writing answers"""

    if request.user.has_perm('exams.change_question'):
        # Check whether user is in "answers_wizard" group
        if request.method == 'POST':
            context = {
                'university': University.objects.get(id=request.POST['university']),
                'course': Course.objects.get(id=request.POST['course']),
                'subject': Subject.objects.get(id=request.POST['subject']),
                'exam': Exam.objects.get(id=request.POST['exam']),
                'exam_questions': Question.objects.filter(exam=request.POST['exam'])
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
        return render(request, 'exams/write_answers.html', context)
    else:
        return HttpResponse(status=403)
