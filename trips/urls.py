# trips/urls.py
from django.urls import path
from .views import QuestionDetailAPIView, UserProfileAPIView, PostUpdateAPIView,PostDetailAPIView# ,CheckRecordsAPIView
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.user_profile, name='user_profile'),  # Profile page URL (e.g., data entry)
    path('profile/manual/', views.manual, name='manual'),  # Manual page URL
    path('profile/manual/function/', views.function, name='function'),
    path('profile/manual/function/road/', views.road, name='road'),  # Road page URL
    path('profile/manual/function/road/route1/', views.route1, name='route1'),
    path('profile/manual/function/road/route2/', views.route2, name='route2'),
    path('profile/manual/function/road/route3/', views.route3, name='route3'),
    path('profile/manual/function/road/route1/arScan1', views.arScan1, name='arScan1'),
    path('profile/manual/function/road/route1/arScan3', views.arScan3, name='arScan3'),
    
    path('api/user/', UserProfileAPIView.as_view(), name='user-create'),#老師寫的
    path('api/question/<int:question_id>/', QuestionDetailAPIView.as_view(), name='question-detail'),#老師寫的
    path('api/post/<str:phone>/', PostUpdateAPIView.as_view(), name='post-update'),#老師寫的

    path('api/post/<str:phone>/detail/', PostDetailAPIView.as_view(), name='post-detail'),  # 新增的 GET 請求端點

    # path('check-records/', CheckRecordsAPIView.as_view(), name='check-records'),
]







