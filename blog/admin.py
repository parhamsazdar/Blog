from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Post

class User_info_inline(admin.StackedInline):
    model = User_info
    can_delete = False
    verbose_name_plural = "مشخصات کاربری"

class UserAdmin(BaseUserAdmin):
    inlines = (User_info_inline,)

class Tags_show(admin.TabularInline):
    model = Post_tags
    extra = 1

class Category_show(admin.TabularInline):
    model = Post_category
    extra = 1

class Comment_show(admin.TabularInline):
    model = Post_comments
    extra = 1

class Post_admin(admin.ModelAdmin):
    inlines = [Tags_show,Category_show,Comment_show]



admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Post,Post_admin)
admin.site.register(Comments)
admin.site.register(Tags)
admin.site.register(Category)


