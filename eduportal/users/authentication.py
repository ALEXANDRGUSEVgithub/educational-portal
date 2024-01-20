from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


# Кастомный бэкенд для аутентификации по электронной почте
class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()  # Получение модели пользователя
        try:
            user = user_model.objects.get(email=username)  # Поиск пользователя по электронной почте
            if user.check_password(password):  # Проверка корректности пароля
                return user  # Возвращаем пользователя в случае успешной аутентификации
            return None  # В случае неправильного пароля возвращаем None
        except (user_model.DoesNotExist, user_model.MultipleObjectsReturned):
            return None  # В случае отсутствия пользователя или неоднозначного результата возвращаем None

    def get_user(self, user_id):
        user_model = get_user_model()  # Получение модели пользователя
        try:
            return user_model.objects.get(pk=user_id)  # Получение пользователя по его идентификатору
        except user_model.DoesNotExist:
            return None  # В случае отсутствия пользователя возвращаем None


# Кастомный бэкенд для аутентификации по номеру телефона
class NumberAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()  # Получение модели пользователя
        try:
            user = user_model.objects.get(phone_number=username)  # Поиск пользователя по номеру телефона
            if user.check_password(password):  # Проверка корректности пароля
                return user  # Возвращаем пользователя в случае успешной аутентификации
            return None  # В случае неправильного пароля возвращаем None
        except (user_model.DoesNotExist, user_model.MultipleObjectsReturned):
            return None  # В случае отсутствия пользователя или неоднозначного результата возвращаем None

    def get_user(self, user_id):
        user_model = get_user_model()  # Получение модели пользователя
        try:
            return user_model.objects.get(pk=user_id)  # Получение пользователя по его идентификатору
        except user_model.DoesNotExist:
            return None  # В случае отсутствия пользователя возвращаем None
