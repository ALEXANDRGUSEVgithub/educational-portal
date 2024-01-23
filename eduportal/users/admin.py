from users.models import User, CategoryUser, GroupStudents
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class CustomUserAdmin(BaseUserAdmin):
    # Поля, которые будут отображаться в админке
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'surname', 'email', 'phone_number', 'date_birth', 'photo')}),
        ('Permissions', {'fields': ('cat_user', 'group_stud', 'courses', 'is_curator', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    # Поля, которые будут отображаться в списке
    list_display = ('username', 'first_name', 'last_name', 'email', 'group_stud', 'cat_user', 'is_curator')

    # Поля, которые будут использоваться в фильтрации
    list_filter = ('cat_user', 'group_stud', 'courses', 'is_curator')

    # Поля для поиска
    search_fields = ('username', 'first_name', 'last_name', 'email')


# Регистрируем модель User и новый класс администратора
admin.site.register(User, CustomUserAdmin)


# Класс для представления модели CategoryUser в админ панели
@admin.register(CategoryUser)
class CategoryUserAdmin(admin.ModelAdmin):
    fields = ['title', ]


# Класс для представления модели GroupStudentsAdmin в админ панели
@admin.register(GroupStudents)
class GroupStudentsAdmin(admin.ModelAdmin):
    fields = ['group', 'slug', 'courses', 'curator', 'members']
    prepopulated_fields = {"slug": ("group",)}
    list_display = ('group', 'slug')