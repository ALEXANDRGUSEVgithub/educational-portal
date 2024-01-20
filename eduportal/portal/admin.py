from django.contrib import admin
from .models import ArticlesAndNews, Category, ShowInfo


admin.site.site_header = "Панель администрирования учебного портала"
admin.site.index_title = "Управление порталом"


# Класс для отображения модели ShowInfo в админ панели
@admin.register(ShowInfo)
class ShowInfoAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'photo', 'file', 'content']
    list_display = ('title',)
    list_display_links = ('title',)


# Класс для отображения модели ArticlesAndNews в админ панели
@admin.register(ArticlesAndNews)
class ArticlesAndNewsAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'photo', 'file', 'content', 'is_published', 'cat']
    list_display = ('title', 'time_create', 'cat', 'is_published')
    list_display_links = ('title', )

    ordering = ['-time_create']
    list_editable = ('is_published',)

    list_per_page = 5
    search_fields = ['title']
    list_filter = ['is_published', 'cat']
    prepopulated_fields = {"slug": ("title",)}

# Класс для отображения модели Category в админ панели
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )
