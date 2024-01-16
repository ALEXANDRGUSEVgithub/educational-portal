from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    surname = models.CharField(max_length=255, blank=True, verbose_name='Отчество')
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name="Фотография")
    date_birth = models.DateTimeField(blank=True, verbose_name="Дата рождения")
    cat_user = models.ForeignKey('CategoryUser', on_delete=models.PROTECT, related_name='users',
                                 default=None, null=True, verbose_name='Категория пользователя')
    group_stud = models.ForeignKey('GroupStudents', blank=True, related_name='groups',
                                   verbose_name='Группа студента', on_delete=models.PROTECT, default=None,
                                   null=True)
    phone_number = models.CharField(max_length=100, unique=True, blank=True, verbose_name='Номер телефона')
    courses = models.ManyToManyField('education.Courses', related_name='course_teacher',
                                    verbose_name='Курсы преподавателя')

    def get_full_name(self):
        return str(self.last_name + ' ' + self.first_name + ' ' + self.surname)

    def get_absolute_url(self):
        return reverse('users:profile_user', kwargs={'user_id': self.pk})

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
    courses = models.ManyToManyField('education.Courses', related_name='groups_related', verbose_name='Курсы')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug')
    curator = models.ForeignKey('User', blank=True, related_name='curator', verbose_name='Куратор группы',
                                on_delete=models.SET_NULL, default=None, null=True)
    members = models.ManyToManyField('User', related_name='group_members', verbose_name='Участники группы')

    def __str__(self):
        return self.group
