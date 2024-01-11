# Generated by Django 4.2.8 on 2024-01-11 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_groupstudents_courses'),
        ('education', '0002_alter_courses_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='group',
            field=models.ManyToManyField(related_name='courses_related', to='users.groupstudents', verbose_name='Группы'),
        ),
    ]
