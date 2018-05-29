from . import models

from rest_framework import serializers


class ExamSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Exam
        fields = (
            'pk',
            'month',
            'year',
            'term',
            'date',
            'total_time',
            'total_marks',
            'exam_code',
        )


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Question
        fields = (
            'pk',
            'question_number',
            'question_body',
            'question_body_image_1',
            'answer',
            'explanation',
            'marks',
            'vote',
        )
