from rest_framework import generics
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post , Question
from .serializers import PostSerializer
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import GameProgress
from django.contrib import messages

def hello_world(request):
    return HttpResponse("Hello World!")

def index(request):
    return render(request, 'index.html')

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
# Create your views here.

@login_required
def user_profile(request):
    if request.method == 'POST':
        phone = request.POST.get('international_phone')
        gender = request.POST.get('gender')
        form = UserProfileForm(request.POST)
        if phone:  # 确保 phone 字段有值
            # 获取或创建 GameProgress 实例
            game_progress, created = GameProgress.objects.get_or_create(phone=phone)
            game_progress.current_stage = 'Initial Stage'  # 根据需要设置初始阶段
            game_progress.history = f"Phone: {phone}, Gender: {gender}"
            game_progress.save()
            form.save()
            messages.success(request, '信息已保存。')
            return redirect('manual')  # 替换为你希望重定向的 URL
        else:
            form = UserProfileForm()

    return render(request, 'user_profile.html')


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