# Generated by Django 4.2.8 on 2024-01-11 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_courses_group'),
        ('users', '0008_groupstudents_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupstudents',
            name='courses',
            field=models.ManyToManyField(related_name='groups_related', to='education.courses', verbose_name='Курсы'),
        ),
    ]
