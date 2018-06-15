from django.http import JsonResponse, HttpResponse
from universities.models import Subject


def get_subjects(request):
    """Handler to return JsonResponse of available subjects"""

    if request.is_ajax():
        course_id = request.POST.get('ci')
        if Subject.objects.filter(course_id=course_id).exists():
            subjects = Subject.objects.filter(
                course_id=course_id).values('id', 'name')
        else:
            return JsonResponse({'no_result': True})
        subjects_list = list()
        for subject in subjects:
            subjects_list.append(subject)
        return JsonResponse(subjects_list, safe=False)
    else:
        return HttpResponse(status=404)
