from django.test import TestCase
import datetime
from .models import University, Course, Subject
from exams.models import Exam, Question


class UniversityTestCase(TestCase):
    """Test case for University"""

    def setUp(self):
        """Setting up test case for University - Saurashtra University"""
        test_university = University.objects.create(name="Saurashtra University",
                                                    university_code="su",
                                                    description="The Saurashtra University is one of the significant universities in Gujarat state in India. This university was established on 23 May 1967 in Rajkot city, the administrative headquarters at Rajkot.",
                                                    founded=datetime.date(
                                                        1967, 5, 23),
                                                    address="Saurashtra University Campus, Rajkot, Gujarat 360005",
                                                    phone="0281 257 8501")

        test_course = Course.objects.create(university=test_university,
                                            name="Computer Engineering",
                                            course_type="full-time",
                                            degree_type="be",
                                            years="4",
                                            description="A computer engineering course",
                                            course_code="su-ce")

        test_subject = Subject.objects.create(course=test_course,
                                              name="Computer Network",
                                              year="2",
                                              subject_code="su-ce-cn")

        test_exam = Exam.objects.create(subject=test_subject,
                                        month="may",
                                        year="2018",
                                        term="summer",
                                        date=datetime.date(2018, 5, 23),
                                        total_time="180",
                                        total_marks=70,
                                        exam_code="su-ce-cn-001")

        test_question = Question.objects.create(exam=test_exam,
                                        question_code="su-ce-cn-001-01",
                                        question_number="1-a-1",
                                        question_body="This is an question!",
                                        question_type="mcq",
                                        answer="This is an answer",
                                        explanation="This doesn't need explanation",
                                        marks=1,
                                        vote=1)

    def test_university_name_and_code(self):
        assert_uni = University.objects.get(university_code="su")
        self.assertEqual(assert_uni.name, 'Saurashtra University')

    def test_course_name_and_code(self):
        assert_course = Course.objects.get(course_code="su-ce")
        self.assertEqual(assert_course.name, 'Computer Engineering')

    def test_subject_name_and_code(self):
        assert_subject = Subject.objects.get(subject_code="su-ce-cn")
        self.assertEqual(assert_subject.name, 'Computer Network')

    def test_exam_and_code(self):
        assert_exam = Exam.objects.get(exam_code="su-ce-cn-001")
        self.assertEqual(assert_exam.month, 'may')
        self.assertEqual(assert_exam.year, '2018')

    def test_question_and_code(self):
        assert_question = Question.objects.get(question_code="su-ce-cn-001-01")
        self.assertEqual(assert_question.question_body, "This is an question!")
