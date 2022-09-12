from django.contrib import admin

from .models import User

@admin.register(User)
class PostModelAdmin(admin.ModelAdmin): #사이트 관리 - users를 추가해주는 코드
    pass