# trips/urls.py
from django.urls import path
from .views import QuestionDetailAPIView, UserProfileCreateAPIView, PostUpdateAPIView
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.user_profile, name='user_profile'),  # Profile page URL (e.g., data entry)
    path('profile/manual/', views.manual, name='manual'),  # Manual page URL
    path('profile/manual/road/', views.road, name='road'),  # Road page URL
    path('profile/manual/road/route1/', views.route1, name='route1'),  # 添加这一行
    path('profile/manual/road/route2/', views.route2, name='route2'),  # 添加这一行
    path('profile/manual/road/route3/', views.route3, name='route3'),  # 添加这一行
    path('profile/manual/road/<int:number>/', views.profile_success, name='profile_success'),
    path('api/user/', UserProfileCreateAPIView.as_view(), name='user-create'),
    path('api/question/<int:question_id>/', QuestionDetailAPIView.as_view(), name='question-detail'),
    path('api/post/<str:phone>/', PostUpdateAPIView.as_view(), name='post-update'),
]






