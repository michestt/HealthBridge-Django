from django.contrib import admin
from .models import Post, Comment, Categories, Likes


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'enabled', 'published')
    ordering = ('-published',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'email', 'date_added')
    ordering = ('-date_added',)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')
    ordering = ('post',)


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Categories)
admin.site.register(Likes, LikeAdmin)
