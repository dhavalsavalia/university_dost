from django.contrib import admin
from django import forms
from .models import Exam, Question, AnswerFeedback
from markdownx.admin import MarkdownxModelAdmin


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


# inherited from MarkdownxModelAdmin to get best best of both
class QuestionAdmin(MarkdownxModelAdmin):
    form = QuestionAdminForm
    list_display = ['question_number', 'question_body',
                    'answer', 'explanation', 'marks', 'upvote', 'downvote']


admin.site.register(Question, QuestionAdmin)


# Answer Feedback Admin
class AnswerFeedbackAdmin(admin.ModelAdmin):

    # want to add link whihc redirects to the question directly
    list_display = [
        'feedback_title', 'created', 'updated', 'feedback_type'
    ]
    search_fields = [
        'feedback_title', 'feedback_body'
    ]
    list_filter = [
        'feedback_type', 'created', 'updated', 'feedback_status'
    ]
    fieldsets = [
        [
            "Feedback",
            {
                "fields": [
                    'feedback_title', 'feedback_body'
                ]
            }],
        [
            "Meta",
            {
                'fields': [
                    'feedback_type', 'feedback_status', 'created',
                    'updated', 'question'
                ]
            }]
    ]
    readonly_fields = [
        'feedback_title', 'created', 'updated', 'feedback_type',
        'feedback_status', 'feedback_body', 'question'
    ]


admin.site.register(AnswerFeedback, AnswerFeedbackAdmin)
