from django.contrib import admin
from django.template.defaultfilters import slugify

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'slug', 'created', 'updated']
    search_fields = ['slug', 'body']
    list_filter = ['created', 'updated']
    prepopulated_fields = {'slug': ('body',)}
    raw_id_fields = ['user']

    def save_model(self, request, obj, form, change):
        if 'body' in form.changed_data:
            obj.slug = slugify(obj.body[:30])
        super().save_model(request, obj, form, change)


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'post', 'is_reply', 'created']
    search_fields = ['user', 'post']
    list_filter = ['created', 'is_reply']
    raw_id_fields = ['user', 'post', 'reply']
