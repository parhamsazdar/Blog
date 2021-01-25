from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Post)
admin.site.register(Writer)
admin.site.register(Comments)
admin.site.register(Tags)
admin.site.register(Category)
admin.site.register(Post_tags)
admin.site.register(Post_category)
admin.site.register(Post_comments)
