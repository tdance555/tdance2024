from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post , Question, UserProfile
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
        except UserProfile.DoesNotExist:
            return Response({"error": "User profile not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(user_profile.post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def hello_world(request):
    return HttpResponse("Hello World!")

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


def profile_success(request, number):
    question = get_object_or_404(Question, number=number)
    return render(request, 'profile_success.html', {'question': question})


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