from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post, Question, UserProfile
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


class UserProfileCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            user_profile = serializer.save()
            return Response(UserProfileSerializer(user_profile).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostUpdateAPIView(APIView):
    def patch(self, request, phone,  *args, **kwargs):
        try:
            user_profile = UserProfile.objects.get(phone=phone)
            post = Post.objects.get(user=user_profile)
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

        content = post.content
        if level in content:
            if level_status is not None:
                content[level]['status'] = level_status
            if user_answer is not None:
                content[level]['user_answer'] = user_answer
            if correct_answer is not None:
                content[level]['correct_answer'] = correct_answer

            post.content = content
            post.save()
            return Response(content[level], status=status.HTTP_200_OK)
        else:
            return Response({"error": "無效的關卡"}, status=status.HTTP_400_BAD_REQUEST)


# def hello_world(request):
#     return HttpResponse("Hello World!")


def index(request):
    return render(request, 'index.html')


class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
# Create your views here.


def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            # 表单成功后重定向到 manual 页面
            return redirect('manual')
    else:
        form = UserProfileForm()

    return render(request, 'user_profile.html', {'form': form})


# def profile_success(request, number):
#     question = get_object_or_404(Question, number=number)
#     return render(request, 'profile_success.html', {'question': question})

def get_api(request):
    return render(request, 'get_api.html')
# AR_scan前身


def ar_scan01(request):
    return render(request, 'ar_scan01.html')


def manual(request):
    return render(request, 'manual.html')


def road(request):
    return render(request, 'road.html')


def route1(request):
    return render(request, 'route1.html')


def route2(request):
    return render(request, 'route2.html')


def route3(request):
    return render(request, 'route3.html')

def function(request):
    return render(request, 'function.html')
