from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import Post, Question, UserProfile,default_content
from .serializers import QuestionSerializer, UserProfileSerializer, PostSerializer
from .forms import UserProfileForm


class QuestionDetailAPIView(APIView):

    def get_object(self, question_id):
        try:
            return Question.objects.get(number=question_id)
        except Question.DoesNotExist:
            return None

    def get(self, request, question_id, *args, **kwargs):
        question_instance = self.get_object(question_id)
        if not question_instance:
            return Response(
                {"res": "Object with question id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = QuestionSerializer(question_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserProfileAPIView(APIView):
    def get(self, request):
        phone = request.query_params.get('phone')
        level = request.query_params.get('level')

        if not phone:
            return Response({"error": "缺少手機號碼"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_profile = UserProfile.objects.get(phone=phone)
        except UserProfile.DoesNotExist:
            return Response({"error": "使用者不存在"}, status=status.HTTP_404_NOT_FOUND)

        try:
            post = Post.objects.get(user=user_profile)
        except Post.DoesNotExist:
            return Response({"error": "使用者遊戲歷程不存在"}, status=status.HTTP_404_NOT_FOUND)

        user_data = UserProfileSerializer(user_profile).data

        if level:
            if not level.isdigit() or int(level) < 1 or int(level) > 29:
                return Response({"error": "無效的關卡參數"}, status=status.HTTP_400_BAD_REQUEST)

            level = str(int(level))
            content = user_data['post']['content']

            if level not in content:
                return Response({"error": "該關卡不存在"}, status=status.HTTP_404_NOT_FOUND)

            return Response({level: content[level]}, status=status.HTTP_200_OK)
        else:
            return Response(user_data, status=status.HTTP_200_OK)


        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            user_profile = serializer.save()
            Post.objects.get_or_create(user=user_profile)
            return Response(UserProfileSerializer(user_profile).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostUpdateAPIView(APIView):
    def patch(self, request, phone, *args, **kwargs):
        try:
            # 獲取或創建與該手機號碼相關的 user_profile 和 post
            user_profile, _ = UserProfile.objects.get_or_create(phone=phone)
            post, created = Post.objects.get_or_create(user=user_profile)
        except UserProfile.DoesNotExist:
            return Response({"error": "User profile not found"}, status=status.HTTP_404_NOT_FOUND)
        except Post.DoesNotExist:
            return Response({"error": "User post not found"}, status=status.HTTP_404_NOT_FOUND)

        level = request.data.get("level")
        level_status = request.data.get('status')
        user_answer = request.data.get('user_answer')
        correct_answer = request.data.get('correct_answer')

        if level is None:
            return Response({"error": "缺少 level 或 data 参数"}, status=status.HTTP_400_BAD_REQUEST)

        # 初始化 content 作為一個空字典（若之前沒有設置 content）
        if post.content is None:
            post.content = {}

        content = post.content

        # 檢查關卡是否存在並更新或創建對應的內容
        if level in content:
            if level_status is not None:
                content[level]['status'] = level_status
            if user_answer is not None:
                content[level]['user_answer'] = user_answer
            if correct_answer is not None:
                content[level]['correct_answer'] = correct_answer
        else:
            content[level] = {
                'status': level_status or '',
                'user_answer': user_answer or '',
                'correct_answer': correct_answer or ''
            }

        # 保存更新
        post.content = content
        post.save()

        return Response(content[level], status=status.HTTP_200_OK)




class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
# Create your views here.


def user_profile(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')

        # 檢查電話號碼是否已存在
        if UserProfile.objects.filter(phone=phone).exists():
            return JsonResponse({'exists': True, 'message': '此手機號碼已經註冊過了'}, status=400)

        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'exists': False, 'redirect_url': '/trips/profile/manual/'})

    else:
        form = UserProfileForm()

    return render(request, 'user_profile.html', {'form': form})



class PostDetailAPIView(APIView):
    def get_object(self, phone):
        try:
            user_profile = UserProfile.objects.get(phone=phone)
            return Post.objects.get(user=user_profile)
        except UserProfile.DoesNotExist:
            return None
        except Post.DoesNotExist:
            return None

    def get(self, request, phone, *args, **kwargs):
        post_instance = self.get_object(phone)
        if not post_instance:
            return Response(
                {"error": "User post not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Extract the content dictionary from the Post instance
        content = post_instance.content

        # Prepare the response data
        response_data = {
            "content": {
                key: {
                    "status": value["status"]
                } for key, value in content.items()
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)

# class CheckStatusAPIView(APIView):
#     def get(self, request, phone):
#         level = request.GET.get('level')
#         if not level:
#             return JsonResponse({'error': 'Level parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             post = Post.objects.get(user__phone=phone)
#         except Post.DoesNotExist:
#             return JsonResponse({'error': 'Post not found for this user'}, status=status.HTTP_404_NOT_FOUND)

#         content = post.content
#         level_status = content.get(level, {}).get('status', 'null')

#         return JsonResponse({'status': level_status})

# class CheckRecordsAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         phone = request.query_params.get('phone')
#         if not phone:
#             return Response({"error": "缺少手機號碼"}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             user_profile = UserProfile.objects.get(phone=phone)
#         except UserProfile.DoesNotExist:
#             return Response({"error": "使用者不存在"}, status=status.HTTP_404_NOT_FOUND)

#         try:
#             post = Post.objects.get(user=user_profile)#UserProfile對象存在，但Post對象不存在，印出此訊息來確認是否找到了對應的 Post 對象。
#             print(f"Found Post for user {user_profile.phone}: {post}")
#         except Post.DoesNotExist:
#             return Response({"error": "使用者遊戲歷程不存在"}, status=status.HTTP_404_NOT_FOUND)

#         user_data = UserProfileSerializer(user_profile).data
#         print(f"Serialized user data: {user_data}")
#         content = user_data['post']['content']

#         response_data = {level: content.get(level, {}) for level in content}

#         return Response(response_data, status=status.HTTP_200_OK)




#各頁面畫面回傳---------------------------------------------------------------------------
def index(request):
    return render(request, 'index.html')

def manual(request):
    return render(request, 'manual.html')

def function(request):
    return render(request, 'function.html')

def road(request):
    return render(request, 'road.html')

def road2(request):
    return render(request, 'road2.html')

def route1(request):
    return render(request, 'route1.html')

def route2(request):
    return render(request, 'route2.html')

def route3(request):
    return render(request, 'route3.html')

def route4(request):
    return render(request, 'route4.html')

def route5(request):
    return render(request, 'route5.html')

def route6(request):
    return render(request, 'route6.html')

def teach(request):
    return render(request, 'teach.html')

#AR頁面回傳---------------------------------------------------------------------------------
def arScan1(request):
    return render(request, 'arScan1.html')

def arScan2(request):
    return render(request, 'arScan2.html')

def arScan3(request):
    return render(request, 'arScan3.html')

def arScan4(request):
    return render(request, 'arScan4.html')

def arScan5(request):
    return render(request, 'arScan5.html')

def arScan6(request):
    return render(request, 'arScan6.html')

def arScan7(request):
    return render(request, 'arScan7.html')

def arScan8(request):
    return render(request, 'arScan8.html')

def arScan9(request):
    return render(request, 'arScan9.html')

def arScan10(request):
    return render(request, 'arScan10.html')

def arScan11(request):
    return render(request, 'arScan11.html')

def arScan12(request):
    return render(request, 'arScan12.html')

def arScan13(request):
    return render(request, 'arScan13.html')

def arScan14(request):
    return render(request, 'arScan14.html')

def arScan15(request):
    return render(request, 'arScan15.html')

def arScan16(request):
    return render(request, 'arScan16.html')

def arScan17(request):
    return render(request, 'arScan17.html')

def arScan18(request):
    return render(request, 'arScan18.html')

def arScan19(request):
    return render(request, 'arScan19.html')

def arScan20(request):
    return render(request, 'arScan20.html')

def arScan21(request):
    return render(request, 'arScan21.html')

def arScan22(request):
    return render(request, 'arScan22.html')

def arScan23(request):
    return render(request, 'arScan23.html')

def arScan24(request):
    return render(request, 'arScan24.html')

def arScan25(request):
    return render(request, 'arScan25.html')

def arScan26(request):
    return render(request, 'arScan26.html')

def arScan27(request):
    return render(request, 'arScan27.html')

def arScan28(request):
    return render(request, 'arScan28.html')

def arScan29(request):
    return render(request, 'arScan29.html')

