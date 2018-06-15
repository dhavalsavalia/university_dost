from django.http import JsonResponse, HttpResponse
from exams.models import Exam


def get_exams(request):
    """Handler to return JsonResponse of available exams"""
    if request.is_ajax():
        subject_id = request.POST.get('si')
        if Exam.objects.filter(subject_id=subject_id).exists():
            exams = Exam.objects.filter(
                subject_id=subject_id).values('id', 'month', 'year')
        else:
            return JsonResponse({'no_result': True})
        exam_list = list()
        for exam in exams:
            exam_list.append(exam)
        return JsonResponse(exam_list, safe=False)
    else:
        return HttpResponse(status=404)
