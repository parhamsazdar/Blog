from functools import partial

from django.contrib import admin, messages
from django.forms import ModelForm
from django.urls import reverse
from django.utils.html import format_html

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










class Post_form(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(Post_form, self).__init__(*args, **kwargs)
        if user is not None:
            user=User.objects.get(user_id=user.pk)
            self.fields['user'].queryset = user

    class Meta:
        model=Post
        fields="__all__"





@admin.register(Post)
class Post_admin(admin.ModelAdmin):
    actions = ["confirm_post", "active_post"]
    readonly_fields = ["confirm", "active"]
    filter_horizontal = ("tags", "category")
    exclude = ("date_pub", "like", "dislike", "comments")
    list_display = ["title", "confirm", "active", "date_pub", "user_style", "like_count", "dislike_count",
                    "comment_count"]

    def like_count(self, obj):
        return obj.like.all().count()

    like_count.admin_order_field = 'like'
    like_count.short_description = 'پسندیده'

    def dislike_count(self, obj):
        return obj.dislike.all().count()

    dislike_count.admin_order_field = 'dislike'
    dislike_count.short_description = 'نپسندیده'

    def comment_count(self, obj):
        return obj.comments.all().count()

    comment_count.admin_order_field = 'comments'
    comment_count.short_description = 'نظرات'

    def user_style(self, obj):
        url = f"/admin/auth/user/{obj.user.pk}/change/"
        return format_html("<a href='{}'>{}</a>", url, obj.user.first_name + " " + obj.user.last_name)

    user_style.admin_order_field = 'user'
    user_style.short_description = 'نویسنده'

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
            self.list_display = ["title", "confirm", "active", "date_pub"]
            self.form=partial(Post_form )
            return qs.filter(user=request.user)
        elif request.user.has_perm("blog.confirm"):
            return qs

    def get_changelist_form(self, request, **kwargs):
        if request.user.has_perm("blog.wirte"):
            self.list_display = ["title", "confirm", "active", "date_pub"]
        return super(Post_admin, self).get_changelist_form(request, **kwargs)

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
    extra = 1


@admin.register(Comments)
class Comments_admin(admin.ModelAdmin):
    inlines = [PostInline]
    actions = ["confirm_post", "active_post"]
    list_display = ["title", "confirm", "active", "like_count", "dislike_count", "date_pub"]
    readonly_fields = ["confirm", "active"]
    exclude = ("date_pub", "like", "dislike")

    def like_count(self, obj):
        return obj.like.all().count()

    like_count.admin_order_field = 'like'
    like_count.short_description = 'پسندیده'

    def dislike_count(self, obj):
        return obj.dislike.all().count()

    dislike_count.admin_order_field = 'dislike'
    dislike_count.short_description = 'نپسندیده'

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


@admin.register(Category)
class Category_admin(admin.ModelAdmin):
    list_display = ["name", "parent_category"]

    def parent_category(self, obj):
        category = ''
        cat = obj
        while cat.parent:
            category += cat.parent.name + " > "
            cat = cat.parent
        category += obj.name
        return category

    parent_category.short_description = "سلسله دسته بندی"


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Tags)
