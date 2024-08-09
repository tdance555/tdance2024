# trips/urls.py
from django.urls import path
from .views import PostListCreate
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/<int:number>/', views.profile_success, name='profile_success'),
    # 其他路由配置

]






