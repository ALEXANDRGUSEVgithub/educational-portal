from django.contrib import admin

from education.models import Courses


# Класс для отображения модели Courses в админ-панели
@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'text', 'group', 'teacher']
    list_display = ('title', )
    list_display_links = ('title', )
    prepopulated_fields = {"slug": ("title",)}
