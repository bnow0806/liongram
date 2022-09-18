from django.contrib import admin
from .models import Inquiry

# Register your models here.
@admin.register(Inquiry)
class PostModelAdmin(admin.ModelAdmin):
    pass