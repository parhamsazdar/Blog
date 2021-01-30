from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class User_info_inline(admin.StackedInline):
    model = User_info
    can_delete = False
    verbose_name_plural = "مشخصات کاربری"

class UserAdmin(BaseUserAdmin):
    inlines = (User_info_inline,)


admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comments)
admin.site.register(Tags)
admin.site.register(Category)
# admin.site.register(Post_tags)
# admin.site.register(Post_category)
# admin.site.register(Post_comments)
