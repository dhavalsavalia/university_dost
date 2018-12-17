from django import forms
from .models import Exam, Question, AnswerFeedback
from markdownx.fields import MarkdownxFormField


class ExamForm(forms.ModelForm):

    class Meta:
        model = Exam
        fields = ['month', 'year', 'term', 'date',
                  'total_time', 'total_marks',
                  'exam_code', 'subject']


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['question_number', 'question_body',
                  'answer', 'explanation', 'marks',
                  'upvote', 'downvote', 'exam', 'author']


class AnswerForm(forms.Form):
    answerfield = MarkdownxFormField()


# Form fields are left blank intentionally
# I will add 'feedback status' field in next updates
class AnswerFeedbackForm(forms.ModelForm):

    class Meta:
        model = AnswerFeedback
        fields = []
