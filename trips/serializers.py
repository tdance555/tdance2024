# trips/serializers.py
from rest_framework import serializers
from .models import Question, UserProfile, Post


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['batch', 'title', 'icon', 'question',
                  'choiceA', 'choiceB', 'choiceC', 'choiceD', 'answer']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['content', 'updated_at']
        read_only_fields = ['updated_at']


class UserProfileSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['phone', 'gender', 'post']

    def create(self, validated_data):
        # 在創建 UserProfile 的同時創建一個關聯的 Post
        user_profile = UserProfile.objects.create(**validated_data)
        Post.objects.create(user=user_profile)
        return user_profile

    def update(self, instance, validated_data):
           instance.phone = validated_data.get('phone', instance.phone)
           instance.gender = validated_data.get('gender', instance.gender)
           instance.save()

           post_data = validated_data.get('post')
           if post_data:
               post_serializer = PostSerializer(instance.post, data=post_data, partial=True)
               if post_serializer.is_valid():
                   post_serializer.save()

           return instance