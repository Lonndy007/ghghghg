from django.urls import path
from .views import  Postivew,PostDetail,PostCreate,PostUpdate,PostDelete


urlpatterns = [
   path('',  Postivew.as_view()),
   path('<int:pk>', PostDetail.as_view()),
   path('create/', PostCreate.as_view(), name='news_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='news_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]
