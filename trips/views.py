from rest_framework import generics
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post , Question
from .serializers import PostSerializer
from .forms import UserProfileForm

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