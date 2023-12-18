from django.contrib import admin
from .models import AuthorCategory, ArticlesAndNews, Category, ShowInfo
# Register your models here.

admin.site.site_header = "Панель администрирования учебного портала"
admin.site.index_title = "Управление порталом"

@admin.register(ShowInfo)
class ShowInfoAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'photo', 'file', 'content']
    list_display = ('title',)
    list_display_links = ('title',)


@admin.register(ArticlesAndNews)
class ArticlesAndNewsAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'photo', 'file', 'content', 'is_published', 'cat', 'author_cat']
    list_display = ('title', 'time_create', 'cat', 'author', 'is_published')
    list_display_links = ('title', )

    ordering = ['-time_create']
    list_editable = ('is_published',)

    list_per_page = 5
    search_fields = ['title']
    list_filter = ['is_published', 'cat', 'author_cat']
    prepopulated_fields = {"slug": ("title",)}



@admin.register(AuthorCategory)
class AuthorCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )
