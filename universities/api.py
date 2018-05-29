from . import models
from . import serializers
from rest_framework import viewsets, permissions


class UniversityViewSet(viewsets.ModelViewSet):
    """ViewSet for the University class"""

    queryset = models.University.objects.all()
    serializer_class = serializers.UniversitySerializer
    permission_classes = [permissions.IsAuthenticated]


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet for the Course class"""

    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubjectViewSet(viewsets.ModelViewSet):
    """ViewSet for the Subject class"""

    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]
