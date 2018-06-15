from django.http import JsonResponse, HttpResponse
from universities.models import Course


def get_courses(request):
    """Handler to return JsonResponse of available courses"""

    if request.is_ajax():
        university_id = request.POST.get('ui')
        if Course.objects.filter(university_id=university_id).exists():
            courses = Course.objects.filter(
                university_id=university_id).values('id', 'name')
        else:
            return JsonResponse({'no_result': True})
        courses_list = list()
        for course in courses:
            courses_list.append(course)
        return JsonResponse(courses_list, safe=False)
    else:
        return HttpResponse(status=404)
