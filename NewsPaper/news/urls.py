from django.urls import path
from .views import  Postivew,PostDetail,PostCreate


urlpatterns = [
   path('',  Postivew.as_view()),
   path('<int:pk>', PostDetail.as_view()),
   path('create/', PostCreate.as_view(), name='news_create'),
]