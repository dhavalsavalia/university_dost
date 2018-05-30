from django.urls import path, include
from rest_framework import routers


from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'university', api.UniversityViewSet)
router.register(r'course', api.CourseViewSet)
router.register(r'subject', api.SubjectViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for University
    path('universities/university/', views.UniversityListView.as_view(),
         name='universities_university_list'),
    path('universities/university/create/', views.UniversityCreateView.as_view(),
         name='universities_university_create'),
    path('universities/university/detail/<int:pk>/',
         views.UniversityDetailView.as_view(), name='universities_university_detail'),
    path('universities/university/update/<int:pk>/',
         views.UniversityUpdateView.as_view(), name='universities_university_update'),
)

urlpatterns += (
    # urls for Course
    path('universities/course/', views.CourseListView.as_view(),
         name='universities_course_list'),
    path('universities/course/create/', views.CourseCreateView.as_view(),
         name='universities_course_create'),
    path('universities/course/detail/<slug:slug>/',
         views.CourseDetailView.as_view(), name='universities_course_detail'),
    path('universities/course/update/<slug:slug>/',
         views.CourseUpdateView.as_view(), name='universities_course_update'),
)

urlpatterns += (
    # urls for Subject
    path('universities/subject/', views.SubjectListView.as_view(),
         name='universities_subject_list'),
    path('universities/subject/create/', views.SubjectCreateView.as_view(),
         name='universities_subject_create'),
    path('universities/subject/detail/<slug:slug>/',
         views.SubjectDetailView.as_view(), name='universities_subject_detail'),
    path('universities/subject/update/<slug:slug>/',
         views.SubjectUpdateView.as_view(), name='universities_subject_update'),
)
