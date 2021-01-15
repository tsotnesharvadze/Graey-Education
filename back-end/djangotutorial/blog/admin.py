from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ['title', 'date', ]
