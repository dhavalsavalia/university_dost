from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from config.settings.base import AUTH_USER_MODEL
from django.db.models.signals import pre_save, post_save
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from universities.models import Subject
from config.utils import (upload_question_body_path,
                          random_string_generator,)


class Exam(models.Model):

    # Choices
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

    # Fields
    month = CharField(max_length=128, choices=MONTH_CHOICES)
    year = CharField(max_length=4)
    term = CharField(max_length=12, choices=TERM_CHOICES)
    date = DateField()
    total_time = CharField(max_length=12)
    total_marks = IntegerField()
    exam_code = CharField(max_length=128, blank=True, null=True)

    # Relationship Fields
    subject = ForeignKey(
        Subject, on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def save(self, *args, **kwargs):
        if self.exam_code and len(self.exam_code.split('-')) > 3:
            self.exam_code = self.exam_code.split('-')[3]
        self.exam_code = '{}-{}'.format(self.subject.subject_code, random_string_generator(size=5))
        qs_exists = Exam.objects.filter(exam_code=self.exam_code).exists()
        if qs_exists:
            self.exam_code = '{}-{}'.format(self.subject.subject_code,
                                            random_string_generator(size=5))
        super(Exam, self).save(*args, **kwargs)

    def __str__(self):
        return self.subject.name + " " + self.term + "-" + self.year

    def get_absolute_url(self):
        return reverse('exams_exam_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('exams_exam_update', args=(self.pk,))


class Question(models.Model):

    # Choices
    QUESTION_TYPE_CHOICES = (
        ('mcq', 'MCQ'),
        ('short_question', 'Short Question'),
        ('descriptive_question', 'Descriptive Question'),
    )

    # Fields
    question_code = models.CharField(max_length=128, blank=True, null=True)
    question_number = models.CharField(max_length=128)
    question_body = models.TextField()
    question_body_image_1 = models.ImageField(
        upload_to=upload_question_body_path, null=True, blank=True)
    question_body_image_2 = models.ImageField(
        upload_to=upload_question_body_path, null=True, blank=True)
    question_body_image_3 = models.ImageField(
        upload_to=upload_question_body_path, null=True, blank=True)
    question_type = models.CharField(
        max_length=12, choices=QUESTION_TYPE_CHOICES)
    answer = models.TextField(blank=True, null=True)
    explanation = models.TextField(blank=True, null=True)
    marks = models.IntegerField()
    vote = models.IntegerField(default=0)

    # Relationship Fields
    exam = ForeignKey(
        Exam, on_delete=models.CASCADE
    )
    author = ForeignKey(
        AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL
    )

    class Meta:
        ordering = ('-pk',)

    def save(self, *args, **kwargs):
        if len(self.question_code.split('-')) > 4:
            self.question_code = self.question_code.split('-')[4]
        self.question_code = '{}-{}'.format(self.exam.exam_code, self.question_code)
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.question_number + " | " + self.exam.term + "-" + self.exam.year

    def get_absolute_url(self):
        return reverse('exams_question_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('exams_question_update', args=(self.pk,))
