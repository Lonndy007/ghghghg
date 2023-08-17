from django.views.generic import ListView,DetailView
from .models import Post


class Postivew(ListView):
    model = Post
    ordering = 'header'
    template_name = 'news.html'
    context_object_name = 'news'

class PostDetail(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'news'
