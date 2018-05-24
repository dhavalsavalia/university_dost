from django.db import models
from universities.models import Subject
from django.db.models.signals import pre_save, post_save
from config.settings.base import AUTH_USER_MODEL
from config.utils import (exam_code_generator,
                          upload_question_body_path)


class Exam(models.Model):
    MONTH_CHOICES = (
        ('january', 'January'),
        ('february', 'February'),
        ('march', 'March'),
        ('april', 'April'),
        ('may', 'May'),
        ('june', 'June'),
        ('july', 'July'),
        ('august', 'August'),
        ('september', 'September'),
        ('october', 'October'),
        ('november', 'November'),
        ('december', 'December')
    )
    TERM_CHOICES = (
        ('summer', 'Summer'),
        ('winter', 'Winter')
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    month = models.CharField(max_length=128, choices=MONTH_CHOICES)
    year = models.CharField(max_length=4)
    term = models.CharField(max_length=12, choices=TERM_CHOICES)
    date = models.DateField()
    total_time = models.CharField(max_length=12)
    total_marks = models.IntegerField()
    exam_code = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return self.subject.name + " " + self.term + "-" + self.year


def pre_save_create_exam_code(sender, instance, *args, **kwargs):
    if not instance.exam_code:
        instance.exam_code = exam_code_generator(instance)

pre_save.connect(pre_save_create_exam_code, sender=Exam)


class Question(models.Model):
    QUESTION_TYPE_CHOICES = (
        ('mcq', 'MCQ'),
        ('short_question', 'Short Question'),
        ('descriptive_question', 'Descriptive Question'),
    )
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    author = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    question_code = models.CharField(max_length=128, blank=True, null=True)
    question_number = models.CharField(max_length=128)
    question_body = models.CharField(max_length=1000)
    question_body_image_1 = models.ImageField(
        upload_to=upload_question_body_path, null=True, blank=True)
    question_body_image_2 = models.ImageField(
        upload_to=upload_question_body_path, null=True, blank=True)
    question_body_image_3 = models.ImageField(
        upload_to=upload_question_body_path, null=True, blank=True)
    question_type = models.CharField(
        max_length=12, choices=QUESTION_TYPE_CHOICES)
    answer = models.TextField()
    explanation = models.TextField(blank=True, null=True)
    marks = models.IntegerField()
    vote = models.IntegerField(default=0)

    def __str__(self):
        return str(self.question_number + "-" + self.exam)
