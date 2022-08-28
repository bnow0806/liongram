from django.contrib import admin

from .models import Post,Comment

#from .models import Post,Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3

# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'content', 'created_at','view_count','writer')
    list_filter = ('created_at',)
    search_fields =('id', 'writer__username')
    search_help_text = 'id, writer__username'
    inlines = [CommentInline]
    actions = ['make_publised']

    def make_publised(modeladmin, request, queryset):
        for item in queryset:
            item.content = "액션에 의한 삭제"
            item.save()

# admin.site.register(Comment)