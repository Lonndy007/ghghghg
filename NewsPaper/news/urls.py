from django.urls import path
from .views import  Postivew


urlpatterns = [
   path('',  Postivew.as_view()),
]