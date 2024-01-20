from django.db import models
from django.urls import reverse


# Класс для определения модели Курсов
class Courses(models.Model):
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    title = models.CharField(max_length=255, verbose_name="Название курса")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug")
    text = models.TextField(blank=True, verbose_name='Основная информация')
    group = models.ManyToManyField('users.GroupStudents', related_name='courses_related', verbose_name='Группы')
    teacher = models.OneToOneField('users.User', on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='teacher', verbose_name='Преподаватель')

    def get_absolute_url(self):
        return reverse('education:course', kwargs={'course_slug': self.slug})

    def __str__(self):
        return self.title
