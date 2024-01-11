from django.db import models


class Courses(models.Model):
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    title = models.CharField(max_length=255, verbose_name="Название курса")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug")
    text = models.TextField(blank=True, verbose_name='Основная информация')
    group = models.ManyToManyField('users.GroupStudents', related_name='courses_related', verbose_name='Группы')

    def __str__(self):
        return self.title
