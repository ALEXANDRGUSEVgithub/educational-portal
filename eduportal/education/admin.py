from django.contrib import admin

from education.models import Courses


# Register your models here.
@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'text', 'group']
    list_display = ('title', )
    list_display_links = ('title', )
    prepopulated_fields = {"slug": ("title",)}