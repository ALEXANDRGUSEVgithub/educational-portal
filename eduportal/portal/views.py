from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from portal.models import ShowInfo, ArticlesAndNews


class PortalHome(ListView):
    model = ArticlesAndNews
    template_name = 'portal/index.html'
    context_object_name = 'posts'

    extra_context = {
        'title': 'Главная страница'
    }

    def get_queryset(self):
        return ArticlesAndNews.published.all()


class ShowMainInfo(DetailView):
    model = ShowInfo
    template_name = 'portal/info.html'
    slug_url_kwarg = 'info_slug'
    context_object_name = 'info'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['info']
        return context


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



