from rest_framework import generics
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
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
            return redirect('profile_success')  # 成功後重定向到成功頁面
    else:
        form = UserProfileForm()

    return render(request, 'user_profile.html', {'form': form})

def profile_success(request):
    return render(request, 'profile_success.html')
