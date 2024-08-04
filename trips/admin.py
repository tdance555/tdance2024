from django.contrib import admin
from .models import Question
from .models import UserProfile

# Register your models here.
admin.site.register(Question)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('gender', 'phone')  # 顯示用戶資訊

admin.site.register(UserProfile, UserProfileAdmin)