from django.contrib import admin
from .models import Question
from .models import UserProfile,GameProgress

# Register your models here.
admin.site.register(Question)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('gender', 'phone')  # 顯示用戶資訊

admin.site.register(UserProfile, UserProfileAdmin)

class GameProgressAdmin(admin.ModelAdmin):
    list_display = ('phone', 'current_stage', 'history')
    search_fields = ('phone', 'current_stage')  # 可搜索的字段

admin.site.register(GameProgress, GameProgressAdmin)