from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.core.validators import RegexValidator


# Класс для формирования формы для авторизации пользователя
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин, E-mail или номер телефона (+79999999999)',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


# Класс для формирования формы для регистрации нового пользователя
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                required=True)
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                required=True)
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)
    first_name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    surname = forms.CharField(label="Отчество", widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    date_birth = forms.DateField(label="Дата рождения", widget=forms.SelectDateWidget(years=range(1940, 2010)),
                                 required=True)
    phone_number = forms.CharField(label="Номер телефона", widget=forms.TextInput(attrs={'class': 'form-control'}),
                                   required=True,
                                   validators=[
                                       RegexValidator(
                                           regex=r'^\+?1?\d{9,15}$',
                                           message="Номер телефона должен быть в формате: +999999999."
                                       ),
                                   ]
                                   )

    class Meta:
        model = get_user_model()
        fields = ['photo', 'username', 'email', 'phone_number', 'first_name', 'last_name', 'surname', 'date_birth',
                  'password1',
                  'password2']
        labels = {
            'email': 'E-mail',
            'first_name': "Имя",
            'last_name': "Фамилия",
            'surname': "Отчество",
            'date_birth': 'Дата рождения',
            'phone_number': 'Номер телефона'
        }
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'date_birth': forms.SelectDateWidget(years=range(1940, 2010)),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    # Проверка email на уникальность
    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email

    # Проверка логина на уникальность
    def clean_username(self):
        username = self.cleaned_data['username']
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return username

    # Проверка номера телефона на уникальность
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if get_user_model().objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Такой номер телефона уже существует!")
        return phone_number


# Класс для определения формы редактирования данных профиля пользователя
class ProfileUserEditForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-input'}))
    phone_number = forms.CharField(disabled=True, label='Номер телефона',
                                   widget=forms.TextInput(attrs={'class': 'form-input'}))
    date_birth = forms.DateField(label="Дата рождения", widget=forms.SelectDateWidget(years=range(1940, 2010)),
                                 required=True)

    class Meta:
        model = get_user_model()
        fields = ['photo', 'username', 'email', 'date_birth', 'first_name', 'last_name', 'surname', 'phone_number']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'surname': 'Отчество'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'surname': forms.TextInput(attrs={'class': 'form-input'}),
        }


# Класс для определения формы изменения пароля
class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label="Подтверждение пароля",
                                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))
