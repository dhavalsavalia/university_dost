from django import forms
from .models import University, Course, Subject


class UniversityForm(forms.ModelForm):

    class Meta:
        model = University
        fields = ['name', 'university_code', 'description',
                  'founded', 'address', 'phone', 'logo']
        widgets = {
            'founded': forms.TextInput(attrs={'cols': 80,
                                              'rows': 1,
                                              'placeholder': 'YYYY-MM-DD'
                                              }),
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


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name',
                                 widget=forms.TextInput(attrs={
                                    'placeholder': 'First Name'
                                    }))
    last_name = forms.CharField(max_length=30, label='Last Name',
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Last Name'
                                    }))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
