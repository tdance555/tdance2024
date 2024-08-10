from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    number = models.PositiveIntegerField(unique=True)
    batch = models.CharField(max_length=100)  # 梯次 第一天,第二天
    route = models.CharField(max_length=1)  #路線名稱 A,B,C
    title = models.CharField(max_length=100) #廠商名稱
    icon = models.URLField(blank=True) #廠商icon
    question = models.CharField(max_length=100) #題目
    choiceA = models.CharField(max_length=100) #選項
    choiceB = models.CharField(max_length=100)
    choiceC = models.CharField(max_length=100)
    choiceD = models.CharField(max_length=100)
    answer = models.CharField(max_length=100) #答案

    def __str__(self):
        return f"{self.number}. {self.question}"

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', '男'),
        ('F', '女'),
        ('O', '其他'),
    ]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.get_gender_display()} - {self.phone}"

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class GameProgress(models.Model):
    phone = models.CharField(max_length=15, default='UNKNOWN')  # 设置默认值
    current_stage = models.CharField(max_length=100)
    history = models.TextField()

    def __str__(self):
        return f"{self.phone} - {self.current_stage}"