from django.db import models
from django.db.models.signals import pre_save, post_save
from config.utils import (upload_university_logo_path,
                          upload_university_cover_path,
                          upload_course_cover_path,
                          upload_subject_cover_path,
                          unique_slug_generator,)


class University(models.Model):
    name = models.CharField(max_length=128)
    university_code = models.CharField(max_length=8)
    description = models.TextField()
    founded = models.DateField()
    address = models.TextField()
    phone = models.CharField(max_length=20)
    logo = models.ImageField(
        upload_to=upload_university_logo_path, null=True, blank=True)
    cover = models.ImageField(
        upload_to=upload_university_cover_path, null=True, blank=True)

    class Meta:
        verbose_name_plural = "universities"

    def __str__(self):
        return self.name


class Course(models.Model):
    COURSE_TYPE_CHOICES = (
        ('full-time', 'Full-Time'),
        ('part-time', 'Part-Time'),
    )
    DEGREE_TYPE_CHOICES = (
        ('be', 'Bachelor of Engineering'),
        ('btech', 'Bachelor of Technology'),
    )
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    course_type = models.CharField(max_length=12, choices=COURSE_TYPE_CHOICES)
    degree_type = models.CharField(max_length=32, choices=DEGREE_TYPE_CHOICES)
    years = models.IntegerField()
    description = models.TextField()
    course_code = models.CharField(max_length=12)
    slug = models.SlugField(blank=True, unique=True)
    cover = models.ImageField(
        upload_to=upload_course_cover_path, null=True, blank=True)

    def __str__(self):
        return self.name


def course_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(course_pre_save_receiver, sender=Course)


class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    year = models.IntegerField()
    subject_code = models.CharField(max_length=128, blank=True, null=True)
    slug = models.SlugField(blank=True, unique=True)
    cover = models.ImageField(
        upload_to=upload_subject_cover_path, null=True, blank=True)

    def __str__(self):
        return self.name


def subject_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(subject_pre_save_receiver, sender=Subject)
