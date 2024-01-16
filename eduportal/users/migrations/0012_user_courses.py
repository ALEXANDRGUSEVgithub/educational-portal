# Generated by Django 4.2.8 on 2024-01-16 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0004_courses_teacher'),
        ('users', '0011_groupstudents_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='courses',
            field=models.ManyToManyField(related_name='course_teacher', to='education.courses', verbose_name='Курсы преподавателя'),
        ),
    ]