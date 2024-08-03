from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .serializers import PostSerializer

def hello_world(request):
    return HttpResponse("Hello World!")

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
# Create your views here.
# Create your views here.
