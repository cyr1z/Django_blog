from django.contrib import admin

# Register your models here.
from .models import User, Genre, Tag, Article, Like, Comment


class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article)
admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(Like)
admin.site.register(Comment)
