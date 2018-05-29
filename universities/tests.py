import unittest
from django.urls import reverse
from django.test import Client
from .models import University, Course, Subject
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


def create_university(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["university_code"] = "university_code"
    defaults["description"] = "description"
    defaults["founded"] = "founded"
    defaults["address"] = "address"
    defaults["phone"] = "phone"
    defaults["logo"] = "logo"
    defaults.update(**kwargs)
    return University.objects.create(**defaults)


def create_course(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["course_type"] = "course_type"
    defaults["degree_type"] = "degree_type"
    defaults["years"] = "years"
    defaults["description"] = "description"
    defaults["course_code"] = "course_code"
    defaults["slug"] = "slug"
    defaults["cover"] = "cover"
    defaults.update(**kwargs)
    if "university" not in defaults:
        defaults["university"] = create_university()
    return Course.objects.create(**defaults)


def create_subject(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["year"] = "year"
    defaults["subject_code"] = "subject_code"
    defaults["slug"] = "slug"
    defaults["cover"] = "cover"
    defaults.update(**kwargs)
    if "course" not in defaults:
        defaults["course"] = create_course()
    return Subject.objects.create(**defaults)


class UniversityViewTest(unittest.TestCase):
    '''
    Tests for University
    '''

    def setUp(self):
        self.client = Client()

    def test_list_university(self):
        url = reverse('universities_university_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_university(self):
        url = reverse('universities_university_create')
        data = {
            "name": "name",
            "university_code": "university_code",
            "description": "description",
            "founded": "founded",
            "address": "address",
            "phone": "phone",
            "logo": "logo",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_university(self):
        university = create_university()
        url = reverse('universities_university_detail', args=[university.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_university(self):
        university = create_university()
        data = {
            "name": "name",
            "university_code": "university_code",
            "description": "description",
            "founded": "founded",
            "address": "address",
            "phone": "phone",
            "logo": "logo",
        }
        url = reverse('universities_university_update', args=[university.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CourseViewTest(unittest.TestCase):
    '''
    Tests for Course
    '''

    def setUp(self):
        self.client = Client()

    def test_list_course(self):
        url = reverse('universities_course_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_course(self):
        url = reverse('universities_course_create')
        data = {
            "name": "name",
            "course_type": "course_type",
            "degree_type": "degree_type",
            "years": "years",
            "description": "description",
            "course_code": "course_code",
            "slug": "slug",
            "cover": "cover",
            "university": create_university().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_course(self):
        course = create_course()
        url = reverse('universities_course_detail', args=[course.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_course(self):
        course = create_course()
        data = {
            "name": "name",
            "course_type": "course_type",
            "degree_type": "degree_type",
            "years": "years",
            "description": "description",
            "course_code": "course_code",
            "slug": "slug",
            "cover": "cover",
            "university": create_university().pk,
        }
        url = reverse('universities_course_update', args=[course.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SubjectViewTest(unittest.TestCase):
    '''
    Tests for Subject
    '''

    def setUp(self):
        self.client = Client()

    def test_list_subject(self):
        url = reverse('universities_subject_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_subject(self):
        url = reverse('universities_subject_create')
        data = {
            "name": "name",
            "year": "year",
            "subject_code": "subject_code",
            "slug": "slug",
            "cover": "cover",
            "course": create_course().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_subject(self):
        subject = create_subject()
        url = reverse('universities_subject_detail', args=[subject.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_subject(self):
        subject = create_subject()
        data = {
            "name": "name",
            "year": "year",
            "subject_code": "subject_code",
            "slug": "slug",
            "cover": "cover",
            "course": create_course().pk,
        }
        url = reverse('universities_subject_update', args=[subject.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
