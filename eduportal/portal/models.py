from django.db import models
from django.urls import reverse


# Create your models here.

class ShowInfo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    photo = models.ImageField(upload_to='photos/', default=None,
                              blank=True, null=True, verbose_name='Фото')
    content = models.TextField(blank=True, verbose_name='Текст статьи')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_info', kwargs={'info_slug': self.slug})
