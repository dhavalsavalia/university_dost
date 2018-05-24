from django.urls import path
from .views import write_answers

urlpatterns = [
    path("write_answers/", write_answers, name="write_answers"),
]