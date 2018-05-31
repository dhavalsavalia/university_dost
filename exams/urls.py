from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'exam', api.ExamViewSet)
router.register(r'question', api.QuestionViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Exam
    path('exams/exam/', views.ExamListView.as_view(), name='exams_exam_list'),
    path('exams/exam/create/', views.ExamCreateView.as_view(),
         name='exams_exam_create'),
    path('exams/exam/detail/<int:pk>/',
         views.ExamDetailView.as_view(), name='exams_exam_detail'),
    path('exams/exam/update/<int:pk>/',
         views.ExamUpdateView.as_view(), name='exams_exam_update'),
)

urlpatterns += (
    # urls for Question
    path('exams/question/', views.QuestionListView.as_view(),
         name='exams_question_list'),
    path('exams/question/create/', views.QuestionCreateView.as_view(),
         name='exams_question_create'),
    path('exams/question/detail/<int:pk>/',
         views.QuestionDetailView.as_view(), name='exams_question_detail'),
    path('exams/question/update/<int:pk>/',
         views.QuestionUpdateView.as_view(), name='exams_question_update'),
)

urlpatterns += (
    # urls for Write Answer
    path('write_answers/', views.write_answers,
         name='write_answers'),
    path('get_courses/', views.get_courses, name='get_courses'),
    path('get_subjects/', views.get_subjects, name='get_subjects'),
    path('get_exams/', views.get_exams, name='get_exams'),
)
