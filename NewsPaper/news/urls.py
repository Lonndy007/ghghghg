from django.urls import path
from .views import  Postivew,PostDetail


urlpatterns = [
   path('',  Postivew.as_view()),

path('<int:pk>', PostDetail.as_view()),
]