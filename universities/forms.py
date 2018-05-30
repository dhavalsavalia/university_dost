from django import forms
from .models import University, Course, Subject


class UniversityForm(forms.ModelForm):

    class Meta:
        model = University
        fields = ['name', 'university_code', 'description',
                  'founded', 'address', 'phone', 'logo']
        widgets={
            'founded': forms.TextInput(attrs={'cols': 80, 'rows': 1, 'placeholder': 'YYYY-MM-DD'}),
        }


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['name', 'course_type', 'degree_type', 'years',
                  'description', 'course_code', 'slug', 'cover', 'university']


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ['name', 'year', 'subject_code', 'slug', 'cover', 'course']
