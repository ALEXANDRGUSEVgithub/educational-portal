from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User, CategoryUser, GroupStudents

# admin.site.register(User, UserAdmin)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['password', 'photo', 'last_login', 'username', 'first_name', 'last_name', 'email',
              'date_birth', 'cat_user', 'group_stud'
              ]
    list_display = ('first_name', 'last_name', 'username', 'group_stud')
    list_display_links = ('first_name', 'username')


@admin.register(CategoryUser)
class CategoryUserAdmin(admin.ModelAdmin):
    fields = ['title', ]


@admin.register(GroupStudents)
class GroupStudentsAdmin(admin.ModelAdmin):
    fields = ['group', 'slug']
    prepopulated_fields = {"slug": ("group",)}
    list_display = ('group', 'slug')