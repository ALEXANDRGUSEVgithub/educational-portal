from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=ArticlesAndNews.Status.PUBLISHED)


class ShowInfo(models.Model):

    class Meta:
        verbose_name = 'Основная информация'
        verbose_name_plural = 'Основная информация'

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    photo = models.ImageField(upload_to='photos/info', default=None,
                              blank=True, null=True, verbose_name='Фото')
    file = models.FileField(upload_to='file/%Y/%m/%d/', default=None,
                            blank=True, null=True, verbose_name='Файлы')
    content = models.TextField(blank=True, verbose_name='Текст статьи')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_info', kwargs={'info_slug': self.slug})


class ArticlesAndNews(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    class Meta:
        verbose_name = 'Статьи и новости'
        verbose_name_plural = 'Статьи и новости'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create']),
        ]

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug',
                            validators=[
                                MinLengthValidator(5, message="Минимум 5 символов"),
                                MaxLengthValidator(100, message="Максимум 100 символов")
                            ])
    file = models.FileField(upload_to='file/%Y/%m/%d/', default=None,
                            blank=True, null=True, verbose_name='Файлы')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None,
                              blank=True, null=True, verbose_name='Фото')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Категории', default=None)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='posts', null=True, default=None,
                               verbose_name='Автор')
    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.title


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')

    def __str__(self):
        return self.title


class UploadFiles(models.Model):
    file = models.FileField(upload_to='uploads_model')

