from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from portal.models import ShowInfo, ArticlesAndNews


# Create your views here.


# def index(request):
#     data = {
#         'title': 'Главная станица',
#     }
#     return render(request, 'portal/index.html', context=data)


class PortalHome(ListView):
    model = ArticlesAndNews
    template_name = 'portal/index.html'
    context_object_name = 'posts'

    extra_context = {
        'title': 'Главная страница'
    }

    def get_queryset(self):
        return ArticlesAndNews.published.all()

def about(request):
    return render(request, 'portal/about.html', context={'title': 'О нас'})


def login(request):
    return HttpResponse('Войти')


def show_info(request, info_slug):
    info = get_object_or_404(ShowInfo, slug=info_slug)

    return render(request, 'portal/info.html', context={'info': info,
                                                        'title': info.title})


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

def show_post(request):
    return HttpResponse('Пост')


