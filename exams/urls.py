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
     path('write_answers/',
          views.write_answers,
          name='write_answers'
          ),
     path('get_courses/',
          views.get_courses,
          name='get_courses'
          ),
     path('get_subjects/',
          views.get_subjects,
          name='get_subjects'
          ),
     path('get_exams/',
          views.get_exams,
          name='get_exams'
          ),
     path('write_answer/<str:exam_pk>/<str:question_pk>/',
          views.write_answer,
          name='write_answer'
          ),
     path('update_answer/',
          views.update_answer,
          name='update_answer'
          ),
     path('view_answers/',
          views.view_answers,
          name='view_answers'
          ),
     path('view_answers/<str:exam_id>/',
          views.view_question_paper,
          name='view_question_paper'
          ),
     path('view_answers/<str:exam_id>/<str:question_id>/',
          views.view_answer,
          name='view_answer'
          ),
     path('view_answers/<str:exam_id>/<str:question_id>/vote/',
          views.vote,
          name='vote'
          ),
     path('view_answers/<str:exam_id>/<str:question_id>/feedback/',
          views.answer_feedback,
          name='answer_feedback'
          ),
)

urlpatterns += (
    # urls for AnswerFeedback
    path('answerfeedback/',
         views.answer_feedback_list,
         name='exams_answerfeedback_list'
         ),
    path('answerfeedback/detail/<int:pk>/',
         views.answer_feedback_detail,
         name='exams_answerfeedback_detail'
         ),
    path('answerfeedback/update/<int:pk>/',
         views.answer_feedback_update,
         name='exams_answerfeedback_update'
         ),
)
