import os
import random
import string
from django.utils.text import slugify


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_university_logo_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=name, ext=ext)
    return "images/university_logo/{final_filename}".format(
        final_filename=final_filename
    )


def upload_university_cover_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=name, ext=ext)
    return "images/university_cover/{final_filename}".format(
        final_filename=final_filename
    )


def upload_course_cover_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=name, ext=ext)
    return "images/course_cover/{final_filename}".format(
        final_filename=final_filename
    )

def upload_subject_cover_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=name, ext=ext)
    return "images/subject_cover/{final_filename}".format(
        final_filename=final_filename
    )


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
