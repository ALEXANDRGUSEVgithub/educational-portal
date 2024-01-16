from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView, DetailView

from eduportal import settings
from users.forms import LoginUserForm, RegisterUserForm, ProfileUserEditForm, UserPasswordChangeForm
from users.models import User


# Create your views here.
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('users:login')


class ProfileUsersView(DetailView):
    model = User
    template_name = 'users/user_profile.html'
    pk_url_kwarg = 'user_id'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль пользователя'
        context['default_image'] = settings.DEFAULT_USER_IMAGE
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs[self.pk_url_kwarg])


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавьте необходимую информацию о профиле
        context['title'] = 'Профиль пользователя'
        context['user'] = self.request.user
        context['default_image'] = settings.DEFAULT_USER_IMAGE
        return context


class ProfileUserEditView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserEditForm
    template_name = 'users/profile_edit.html'
    extra_context = {
        'title': "Редактирование профиля",
        'default_image': settings.DEFAULT_USER_IMAGE,
    }

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"
    extra_context = {'title': "Изменение пароля"}
