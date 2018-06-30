from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from exams.models import Exam, Question
from universities.models import University, Course, Subject


@login_required
def view_answers(request):
    """Main entry-point to view answers"""


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
    return render(request, 'exams/view_answer_select_exam.html', context)


@login_required
def view_question_paper(request, exam_id):
    
    exam = Exam.objects.get(id=exam_id)
    exam_questions = Question.objects.filter(exam_id=exam_id).order_by('question_code')
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
    context = {
        'univquestionersity': question.exam.subject.course.university,
        'course': question.exam.subject.course,
        'subject': question.exam.subject,
        'exam': question.exam,
        'question': question,

        # a litter hack to get previous question
        'prev_question': (Question.objects
                        .filter(exam=question.exam, question_number__lte=question.question_number, id__lt=question.id)
                        .exclude(id=question.id)
                        .order_by('-question_number',)
                        .first()),

        # another litter hack to get next question
        'next_question': (Question.objects
                        .filter(exam=question.exam, question_number__gte=question.question_number, id__gt=question.id)
                        .exclude(id=question.id)
                        .order_by('question_number')
                        .first())
    }
    return render(request, 'exams/view_answer.html', context)