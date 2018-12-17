from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from exams.models import Question
from universities.models import University


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    # ManyToMany with questions
    questions = models.ManyToManyField(Question, related_name='questions')

    # voted_questions is actually voted answers
    # fuck this is confusing
    upvoted_questions = models.ManyToManyField(
                                        Question,
                                        related_name='upvoted_questions'
                                        )
    downvoted_questions = models.ManyToManyField(
                                        Question,
                                        related_name='downvoted_questions'
                                        )

    # Additional Fields
    semester = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    university = models.ForeignKey(University,
                                   related_name='university',
                                   on_delete=models.CASCADE,
                                   blank=True,
                                   null=True
                                   )
    weekly_test = models.BooleanField(default=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
