from . import models

from rest_framework import serializers


class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.University
        fields = (
            'pk',
            'name',
            'university_code',
            'description',
            'founded',
            'address',
            'phone',
            'logo',
        )


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = (
            'slug',
            'name',
            'course_type',
            'degree_type',
            'years',
            'description',
            'course_code',
            'cover',
        )


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Subject
        fields = (
            'slug',
            'name',
            'year',
            'subject_code',
            'cover',
        )
