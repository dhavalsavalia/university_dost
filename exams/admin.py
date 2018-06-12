from django.contrib import admin
from django import forms
from .models import Exam, Question


class ExamAdminForm(forms.ModelForm):

    class Meta:
        model = Exam
        fields = '__all__'


class ExamAdmin(admin.ModelAdmin):
    form = ExamAdminForm
    list_display = ['month', 'year', 'term', 'date',
                    'total_time', 'total_marks', 'exam_code']
    list_filter = ['term', 'year', 'subject']

admin.site.register(Exam, ExamAdmin)


class QuestionAdminForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = '__all__'


class QuestionAdmin(admin.ModelAdmin):
    form = QuestionAdminForm
    list_display = ['question_number', 'question_body',
                    'question_body_image_1', 'answer', 'explanation', 'marks', 'vote']


admin.site.register(Question, QuestionAdmin)
