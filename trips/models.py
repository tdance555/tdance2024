from django.db import models

# Create your models here.
def default_content():
    return {
        "1": {
            "status": "null", # null, pass, fail
            "user_answer": "",
            "correct_answer": "",
        },
        "2": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "3": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "4": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "5": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "6": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "7": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "8": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "9": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "10": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "11": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "12": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "13": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "14": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "15": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "16": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "17": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "18": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "19": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "20": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "21": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "22": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "23": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "24": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "25": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "26": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "27": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "28": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
        "29": {
            "status": "null",
            "user_answer": "",
            "correct_answer": "",
        },
    }


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

    phone = models.CharField(max_length=15, primary_key=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.get_gender_display()} - {self.phone}"

class Post(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.SET_NULL, related_name='post', null=True, blank=True)
    content = models.JSONField(default=default_content)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Post by {self.user.phone} at {self.created_at}"
# class Post1(models.Model):
#     number = models.PositiveIntegerField()
#     title = models.CharField(max_length=100)
#     content = models.TextField(blank=True)
#     image = models.ImageField(upload_to='questions/', blank=True, null=True)

#     def __str__(self):
#         return f"{self.number}. {self.title}"