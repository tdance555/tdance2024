# trips/urls.py
from django.urls import path
from .views import PostListCreate
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('profile/', views.user_profile, name='user_profile'),  # Profile page URL (e.g., data entry)
    path('profile/manual/', views.manual, name='manual'),  # Manual page URL
    path('profile/manual/road/', views.road, name='road'),  # Road page URL
    path('profile/manual/road/route1/', views.route1, name='route1'),  # 添加这一行
    path('profile/manual/road/route2/', views.route2, name='route2'),  # 添加这一行
    path('profile/manual/road/route3/', views.route3, name='route3'),  # 添加这一行
    path('profile/manual/road/<int:number>/', views.profile_success, name='profile_success'),

]






