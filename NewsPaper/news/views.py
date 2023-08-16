from django.views.generic import ListView,DetailView
from .models import Post


class Postivew(ListView):
    model = Post
    ordering = 'header'
    template_name = 'news.html'
    context_object_name = 'news'

class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'news.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'news'
