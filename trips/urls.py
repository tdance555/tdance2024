# trips/urls.py
from django.urls import path
from .views import QuestionDetailAPIView, UserProfileAPIView, PostUpdateAPIView,PostDetailAPIView#,CheckStatusAPIView
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.user_profile, name='user_profile'),  # Profile page URL (e.g., data entry)
    path('profile/manual/', views.manual, name='manual'),  # Manual page URL
    path('profile/manual/function/', views.function, name='function'),
    path('profile/manual/function/road/', views.road, name='road'),  # Road page URL
    path('profile/manual/function/road/route1/', views.route1, name='route1'),  # 添加这一行
    path('profile/manual/function/road/route2/', views.route2, name='route2'),  # 添加这一行
    path('profile/manual/function/road/route3/', views.route3, name='route3'),  # 添加这一行
    path('profile/manual/function/road/route1/arScan1', views.arScan1, name='arScan1'),
    
    # path('get_api/', views.get_api, name='get_api'),
    path('api/user/', UserProfileAPIView.as_view(), name='user-create'),
    path('api/question/<int:question_id>/', QuestionDetailAPIView.as_view(), name='question-detail'),
    path('api/post/<str:phone>/', PostUpdateAPIView.as_view(), name='post-update'),
    path('api/post-detail/<str:phone>/', PostDetailAPIView.as_view(), name='post-detail'),

    # path('api/check-status/<str:phone>/', CheckStatusAPIView.as_view(), name='check-status'),
]






