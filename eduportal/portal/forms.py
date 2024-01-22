from django import forms
from django.core.exceptions import ValidationError

from portal.models import ArticlesAndNews


# Класс для определения формы добавления нового поста
class AddPostForm(forms.ModelForm):

    class Meta:
        model = ArticlesAndNews
        fields = ['title', 'slug', 'content', 'photo', 'file', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        labels = {'slug': 'URL'}

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError("Длина превышает 50 символов")

        return title