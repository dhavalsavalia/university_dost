# Generated by Django 2.0.5 on 2018-05-24 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_auto_20180524_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_code',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]