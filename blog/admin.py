from django.contrib import admin, messages
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


# class Tags_show(admin.TabularInline):
#     model = Post_tags
#     extra = 1

#
# class Category_show(admin.TabularInline):
#     model = Post_category
#     extra = 1
#

# class Comment_show(admin.TabularInline):
#     model = Post_comments
#     extra = 1


class Post_admin(admin.ModelAdmin):
    actions = ["confirm_post", "active_post"]
    list_display = ["title", "confirm", "active"]
    readonly_fields = ["confirm", "active", "like", "dislike", "date_pub"]
    filter_horizontal = ("tags", "category","comments")

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.has_perm("blog.confirm") is False:
            if 'confirm_post' in actions:
                del actions['confirm_post']
        if request.user.has_perm("blog.active") is False:
            if 'active' in actions:
                del actions['active']
        return actions

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.has_perm("blog.wirte"):
            # admin.site.disable_action('confirm_approval')
            return qs.filter(user=request.user)
        elif request.user.has_perm("blog.confirm"):
            return qs

    def confirm_post(self, request, queryset):
        queryset.update(confirm=True)
        self.message_user(request, "پست مورد نظر تایید شد", messages.SUCCESS)

    def active_post(self, request, queryset):
        queryset.update(active=True)
        self.message_user(request, "پست مورد نظر فعال شد", messages.SUCCESS)

    confirm_post.short_description = 'تایید کردن پست'
    active_post.short_description = 'فعال کردن پست'

    def get_changeform_initial_data(self, request):
        get_data = super(Post_admin, self).get_changeform_initial_data(request)
        get_data['user'] = request.user.pk
        return get_data


class PostInline(admin.TabularInline):
    model = Post.comments.through

class Comments_admin(admin.ModelAdmin):
    inlines = [PostInline]
    actions = ["confirm_post", "active_post"]
    list_display = ["title", "confirm", "active"]
    readonly_fields = ["confirm", "active", "like", "dislike", "date_pub"]


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.has_perm("blog.wirte"):
            # admin.site.disable_action('confirm_approval')
            return qs.filter(post__user=request.user)
        elif request.user.has_perm("blog.confirm"):
            return qs

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.has_perm("blog.confirm") is False:
            if 'confirm_post' in actions:
                del actions['confirm_post']
        if request.user.has_perm("blog.active") is False:
            if 'active' in actions:
                del actions['active']
        return actions

    def confirm_comment(self, request, queryset):
        queryset.update(confirm=True)
        self.message_user(request, "پست مورد نظر تایید شد", messages.SUCCESS)

    confirm_comment.short_description = 'تایید کردن نظر'

    def active_comment(self, request, queryset):
        queryset.update(active=True)
        self.message_user(request, "پست مورد نظر فعال شد", messages.SUCCESS)

    active_comment.short_description = 'فعال کردن نظر'


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Post, Post_admin)
admin.site.register(Comments,Comments_admin)
admin.site.register(Tags)
admin.site.register(Category)
