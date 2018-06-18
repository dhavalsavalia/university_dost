from django import forms
from .models import Exam, Question
from markdownx.fields import MarkdownxFormField


class ExamForm(forms.ModelForm):

    class Meta:
        model = Exam
        fields = ['month', 'year', 'term', 'date',
                  'total_time', 'total_marks', 'exam_code', 'subject']


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['question_number', 'question_body', 'question_body_image_1',
                  'answer', 'explanation', 'marks', 'vote', 'exam', 'author']


class AnswerForm(forms.Form):
    answerfield = MarkdownxFormField()
