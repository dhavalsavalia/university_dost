# Generated by Django 2.0.5 on 2018-05-29 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0002_auto_20180523_1542'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('-pk',)},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ('-pk',)},
        ),
        migrations.AlterModelOptions(
            name='university',
            options={'ordering': ('-pk',)},
        ),
        migrations.RemoveField(
            model_name='university',
            name='cover',
        ),
    ]
