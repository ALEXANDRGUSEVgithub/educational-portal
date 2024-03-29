# Generated by Django 4.2.8 on 2024-01-09 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_groupstudents_user_group_stud'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='groupstudents',
            name='group',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='groupstudents',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='user',
            name='cat_user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='users', to='users.categoryuser', verbose_name='Категория пользователя'),
        ),
    ]
