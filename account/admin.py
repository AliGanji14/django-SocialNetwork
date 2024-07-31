from django.contrib import admin

from .models import Relation


@admin.register(Relation)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['from_user', 'to_user']
    list_filter = ['from_user', 'to_user', 'created']
    raw_id_fields = ['from_user', 'to_user']
