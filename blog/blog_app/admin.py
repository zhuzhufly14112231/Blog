from django.contrib import admin
from .models import Post,Comment
# Register your models here.

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    # 右侧的展示
    list_filter = ('status','create','publish','author')
    search_fields = ('title','body')
    raw_id_fields = ('author',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','post','create','active')
    list_filter = ('active','create','update')
    search_fields = ('name','email','body')




