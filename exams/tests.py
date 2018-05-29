import unittest
from django.urls import reverse
from django.test import Client
from .models import Exam, Question
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_exam(**kwargs):
    defaults = {}
    defaults["month"] = "month"
    defaults["year"] = "year"
    defaults["term"] = "term"
    defaults["date"] = "date"
    defaults["total_time"] = "total_time"
    defaults["total_marks"] = "total_marks"
    defaults["exam_code"] = "exam_code"
    defaults.update(**kwargs)
    if "subject" not in defaults:
        defaults["subject"] = create_subject()
    return Exam.objects.create(**defaults)


def create_question(**kwargs):
    defaults = {}
    defaults["question_number"] = "question_number"
    defaults["question_body"] = "question_body"
    defaults["question_body_image_1"] = "question_body_image_1"
    defaults["answer"] = "answer"
    defaults["explanation"] = "explanation"
    defaults["marks"] = "marks"
    defaults["vote"] = "vote"
    defaults.update(**kwargs)
    if "exam" not in defaults:
        defaults["exam"] = create_exam()
    if "author" not in defaults:
        defaults["author"] = create_auth_user_model()
    return Question.objects.create(**defaults)


class ExamViewTest(unittest.TestCase):
    '''
    Tests for Exam
    '''

    def setUp(self):
        self.client = Client()

    def test_list_exam(self):
        url = reverse('app_name_exam_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_exam(self):
        url = reverse('app_name_exam_create')
        data = {
            "month": "month",
            "year": "year",
            "term": "term",
            "date": "date",
            "total_time": "total_time",
            "total_marks": "total_marks",
            "exam_code": "exam_code",
            "subject": create_subject().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_exam(self):
        exam = create_exam()
        url = reverse('app_name_exam_detail', args=[exam.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_exam(self):
        exam = create_exam()
        data = {
            "month": "month",
            "year": "year",
            "term": "term",
            "date": "date",
            "total_time": "total_time",
            "total_marks": "total_marks",
            "exam_code": "exam_code",
            "subject": create_subject().pk,
        }
        url = reverse('app_name_exam_update', args=[exam.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class QuestionViewTest(unittest.TestCase):
    '''
    Tests for Question
    '''

    def setUp(self):
        self.client = Client()

    def test_list_question(self):
        url = reverse('app_name_question_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_question(self):
        url = reverse('app_name_question_create')
        data = {
            "question_number": "question_number",
            "question_body": "question_body",
            "question_body_image_1": "question_body_image_1",
            "answer": "answer",
            "explanation": "explanation",
            "marks": "marks",
            "vote": "vote",
            "exam": create_exam().pk,
            "author": create_auth_user_model().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_question(self):
        question = create_question()
        url = reverse('app_name_question_detail', args=[question.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_question(self):
        question = create_question()
        data = {
            "question_number": "question_number",
            "question_body": "question_body",
            "question_body_image_1": "question_body_image_1",
            "answer": "answer",
            "explanation": "explanation",
            "marks": "marks",
            "vote": "vote",
            "exam": create_exam().pk,
            "author": create_auth_user_model().pk,
        }
        url = reverse('app_name_question_update', args=[question.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
