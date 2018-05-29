from django.contrib import admin
from django import forms
from .models import University, Course, Subject


class UniversityAdminForm(forms.ModelForm):

    class Meta:
        model = University
        fields = '__all__'


class UniversityAdmin(admin.ModelAdmin):
    form = UniversityAdminForm
    list_display = ['name', 'university_code',
                    'description', 'founded', 'address', 'phone', 'logo']
    readonly_fields = ['name', 'university_code',
                       'description', 'founded', 'address', 'phone', 'logo']

admin.site.register(University, UniversityAdmin)


class CourseAdminForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'


class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm
    list_display = ['name', 'course_type', 'degree_type',
                    'years', 'description', 'course_code', 'slug', 'cover']
    readonly_fields = ['name', 'course_type', 'degree_type',
                       'years', 'description', 'course_code', 'slug', 'cover']

admin.site.register(Course, CourseAdmin)


class SubjectAdminForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = '__all__'


class SubjectAdmin(admin.ModelAdmin):
    form = SubjectAdminForm
    list_display = ['name', 'year', 'subject_code', 'slug', 'cover']
    readonly_fields = ['name', 'year', 'subject_code', 'slug', 'cover']

admin.site.register(Subject, SubjectAdmin)
