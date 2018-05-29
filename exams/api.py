from . import models
from . import serializers
from rest_framework import viewsets, permissions


class ExamViewSet(viewsets.ModelViewSet):
    """ViewSet for the Exam class"""

    queryset = models.Exam.objects.all()
    serializer_class = serializers.ExamSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Question class"""

    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]
