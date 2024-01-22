from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

from portal.forms import AddPostForm
from portal.models import ShowInfo, ArticlesAndNews


# Класс для отображения постов на главной странице
class PortalHome(ListView):
    model = ArticlesAndNews
    template_name = 'portal/index.html'
    context_object_name = 'posts'

    extra_context = {
        'title': 'Главная страница'
    }

    def get_queryset(self):
        return ArticlesAndNews.published.all()


# Класс для отображения основной информации
class ShowMainInfo(DetailView):
    model = ShowInfo
    template_name = 'portal/info.html'
    slug_url_kwarg = 'info_slug'
    context_object_name = 'info'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['info']
        return context


# Класс для отображения поста для чтения
class ShowPost(DetailView):
    model = ArticlesAndNews
    template_name = 'portal/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(ArticlesAndNews.published, slug=self.kwargs[self.slug_url_kwarg])


# Класс для добавления нового поста на сайта
class AddPage(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'portal/addpage.html'
    title_page = 'Добавление статьи'
    permission_required = 'women.add_women'

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)



