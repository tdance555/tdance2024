# trips/urls.py
from django.urls import path
from .views import PostListCreate
from . import views
urlpatterns = [
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/success/', views.profile_success, name='profile_success'),
    path('profile/', views.user_profile, name='user_profile'),
]

#,sdfghjkjnh;gfdjhgd




