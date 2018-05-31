from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django.db.models.signals import pre_save, post_save
from django_extensions.db import fields as extension_fields
from config.utils import (upload_university_logo_path,
                          upload_university_cover_path,
                          upload_course_cover_path,
                          upload_subject_cover_path,
                          unique_slug_generator,)


class University(models.Model):

    # Fields
    name = CharField(max_length=128)
    university_code = CharField(max_length=8)
    description = TextField()
    founded = DateField()
    address = TextField()
    phone = CharField(max_length=20)
    logo = ImageField(upload_to=upload_university_logo_path,
                      null=True, blank=True)
    cover = models.ImageField(
        upload_to=upload_university_cover_path, null=True, blank=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = "universities"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('universities_university_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('universities_university_update', args=(self.pk,))


class Course(models.Model):

    # Choices
    COURSE_TYPE_CHOICES = (
        ('full-time', 'Full-Time'),
        ('part-time', 'Part-Time'),
    )
    DEGREE_TYPE_CHOICES = (
        ('be', 'Bachelor of Engineering'),
        ('btech', 'Bachelor of Technology'),
    )

    # Fields
    name = CharField(max_length=128)
    course_type = CharField(max_length=12, choices=COURSE_TYPE_CHOICES)
    degree_type = CharField(max_length=32, choices=DEGREE_TYPE_CHOICES)
    years = IntegerField()
    description = TextField()
    course_code = CharField(max_length=12)
    slug = SlugField(blank=True, unique=True)
    cover = ImageField(upload_to=upload_course_cover_path,
                       null=True, blank=True)

    # Relationship Fields
    university = ForeignKey(
        University,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.name+"-"+self.university.university_code

    def get_absolute_url(self):
        return reverse('universities_course_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('universities_course_update', args=(self.slug,))


def course_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(course_pre_save_receiver, sender=Course)


class Subject(models.Model):

    # Fields
    name = CharField(max_length=128)
    year = IntegerField()
    subject_code = CharField(max_length=128, blank=True, null=True)
    slug = SlugField(blank=True, unique=True)
    cover = ImageField(upload_to=upload_subject_cover_path,
                       null=True, blank=True)

    # Relationship Fields
    course = ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('universities_subject_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('universities_subject_update', args=(self.slug,))


def subject_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(subject_pre_save_receiver, sender=Subject)
