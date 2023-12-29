from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name="Фотография")
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name="Дата рождения")
    cat_user = models.ForeignKey('CategoryUser', on_delete=models.PROTECT, related_name='users',
                                 default=None, null=True, verbose_name='Категория пользователя')
    group_stud = models.ForeignKey('GroupStudents', blank=True, related_name='groups',
                                        verbose_name='Группа студента', on_delete=models.PROTECT, default=None,
                                   null=True)

    def __str__(self):
        return self.username


class CategoryUser(models.Model):
    class Meta:
        verbose_name = 'Категория пользователя'
        verbose_name_plural = 'Категории пользователей'

    title = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.title


class GroupStudents(models.Model):
    class Meta:
        verbose_name = 'Группы студентов'
        verbose_name_plural = 'Группа студентов'

    group = models.CharField(max_length=100, db_index=True, verbose_name='Группа')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug')

    def __str__(self):
        return self.group