from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Relation, Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class ExtendedUserAdmin(UserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), ExtendedUserAdmin)


@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    list_display = ['from_user', 'to_user', 'created']
    search_fields = ['from_user', 'to_user']
    list_filter = ['created']
    raw_id_fields = ['from_user', 'to_user']
