from django.contrib import admin
from django import forms
from .models import University, Course, Subject


class UniversityAdminForm(forms.ModelForm):

    class Meta:
        model = University
        fields = '__all__'


class UniversityAdmin(admin.ModelAdmin):
    form = UniversityAdminForm
    list_display = ['name', 'university_code', 'address', 'phone']


admin.site.register(University, UniversityAdmin)


class CourseAdminForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'


class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm
    list_display = ['name', 'course_code', 'slug']
    list_filter = ['university']

admin.site.register(Course, CourseAdmin)


class SubjectAdminForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = '__all__'


class SubjectAdmin(admin.ModelAdmin):
    form = SubjectAdminForm
    list_display = ['name', 'year', 'subject_code', 'course']
    list_filter = ['course__university', 'year', 'course__name']


admin.site.register(Subject, SubjectAdmin)
