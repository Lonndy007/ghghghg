import django_filters
from django_filters import FilterSet
from .models import Post

class PostFilter(FilterSet):
    release_year__gt = django_filters.NumberFilter(field_name='release_date', lookup_expr='year__gt')



    class Meta:
       model = Post

       fields = {
           # поиск по названию
           'header': ['icontains'],
           'author':['exact'],
       }