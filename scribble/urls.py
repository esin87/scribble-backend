from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<int:pk>', views.PostDetail.as_view(), name='post_detail'),
]
