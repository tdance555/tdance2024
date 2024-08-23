# trips/urls.py
from django.urls import path
from .views import QuestionDetailAPIView, UserProfileAPIView, PostUpdateAPIView,PostDetailAPIView#,CheckStatusAPIView
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.user_profile, name='user_profile'),  # Profile page URL (e.g., data entry)
    path('profile/manual/', views.manual, name='manual'),  # Manual page URL
    path('profile/manual/function/', views.function, name='function'),
    path('profile/manual/function/teach', views.teach, name='teach'),
    path('profile/manual/function/road/', views.road, name='road'),  # Road page URL
    path('profile/manual/function/road2/', views.road2, name='road2'),
    path('profile/manual/function/road/route1/', views.route1, name='route1'),  # 添加这一行
    path('profile/manual/function/road/route2/', views.route2, name='route2'),  # 添加这一行
    path('profile/manual/function/road/route3/', views.route3, name='route3'),  # 添加这一行
    path('profile/manual/function/road2/route4/', views.route4, name='route4'),
    path('profile/manual/function/road2/route5/', views.route5, name='route5'),
    path('profile/manual/function/road2/route6/', views.route6, name='route6'),

    # AR頁面---------------------------------------------------------------------------------------------------
    # 第一梯次
    path('profile/manual/function/road/route1/arScan1', views.arScan1, name='arScan1'),
    path('profile/manual/function/road/route1/arScan2', views.arScan2, name='arScan2'),
    path('profile/manual/function/road/route1/arScan3', views.arScan3, name='arScan3'),
    path('profile/manual/function/road/route1/arScan4', views.arScan4, name='arScan4'),
    path('profile/manual/function/road/route1/arScan5', views.arScan5, name='arScan5'),
    path('profile/manual/function/road/route1/arScan18', views.arScan18, name='arScan18'),

    path('profile/manual/function/road/route2/arScan6', views.arScan6, name='arScan6'),
    path('profile/manual/function/road/route2/arScan7', views.arScan7, name='arScan7'),
    path('profile/manual/function/road/route2/arScan8', views.arScan8, name='arScan8'),
    path('profile/manual/function/road/route2/arScan9', views.arScan9, name='arScan9'),
    path('profile/manual/function/road/route2/arScan10', views.arScan10, name='arScan10'),
    path('profile/manual/function/road/route2/arScan11', views.arScan11, name='arScan11'),

    path('profile/manual/function/road/route3/arScan12', views.arScan12, name='arScan12'),
    path('profile/manual/function/road/route3/arScan13', views.arScan13, name='arScan13'),
    path('profile/manual/function/road/route3/arScan14', views.arScan14, name='arScan14'),
    path('profile/manual/function/road/route3/arScan15', views.arScan15, name='arScan15'),
    path('profile/manual/function/road/route3/arScan16', views.arScan16, name='arScan16'),
    path('profile/manual/function/road/route3/arScan17', views.arScan17, name='arScan17'),

    # 第二梯次
    path('profile/manual/function/road2/route4/arScan1', views.arScan1, name='arScan1'),
    path('profile/manual/function/road2/route4/arScan2', views.arScan2, name='arScan2'),
    path('profile/manual/function/road2/route4/arScan3', views.arScan3, name='arScan3'),
    path('profile/manual/function/road2/route4/arScan4', views.arScan4, name='arScan4'),
    path('profile/manual/function/road2/route4/arScan5', views.arScan5, name='arScan5'),
    path('profile/manual/function/road2/route4/arScan29', views.arScan29, name='arScan29'),

    path('profile/manual/function/road2/route5/arScan6', views.arScan6, name='arScan6'),
    path('profile/manual/function/road2/route5/arScan7', views.arScan7, name='arScan7'),
    path('profile/manual/function/road2/route5/arScan19', views.arScan19, name='arScan19'),
    path('profile/manual/function/road2/route5/arScan20', views.arScan20, name='arScan20'),
    path('profile/manual/function/road2/route5/arScan21', views.arScan21, name='arScan21'),
    path('profile/manual/function/road2/route5/arScan22', views.arScan22, name='arScan22'),

    path('profile/manual/function/road2/route6/arScan23', views.arScan23, name='arScan23'),
    path('profile/manual/function/road2/route6/arScan24', views.arScan24, name='arScan24'),
    path('profile/manual/function/road2/route6/arScan25', views.arScan25, name='arScan25'),
    path('profile/manual/function/road2/route6/arScan26', views.arScan26, name='arScan26'),
    path('profile/manual/function/road2/route6/arScan27', views.arScan27, name='arScan27'),
    path('profile/manual/function/road2/route6/arScan28', views.arScan28, name='arScan28'),

    # API調用----------------------------------------------------------------------------------------------------
    # path('get_api/', views.get_api, name='get_api'),
    path('api/user/', UserProfileAPIView.as_view(), name='user-create'),
    path('api/question/<int:question_id>/', QuestionDetailAPIView.as_view(), name='question-detail'),
    path('api/post/<str:phone>/', PostUpdateAPIView.as_view(), name='post-update'),
    path('api/post-detail/<str:phone>/', PostDetailAPIView.as_view(), name='post-detail'),

    # path('api/check-status/<str:phone>/', CheckStatusAPIView.as_view(), name='check-status'),
]






