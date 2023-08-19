from django.views.generic import ListView,DetailView
from .models import Post
from .filters import PostFilter


class Postivew(ListView):
    model = Post
    ordering = 'header'
    template_name = 'news.html'
    context_object_name = 'news'

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

class PostDetail(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'news'
    paginate_by = 2
