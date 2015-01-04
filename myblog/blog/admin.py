from django.contrib import admin
from models import Blog, Category, Comment


class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    exclude = ['posted']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comment)
