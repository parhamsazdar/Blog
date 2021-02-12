from django.urls import path, include

from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index"),
    path('post/<int:post_id>', views.post_show, name='post_show'),
    path('cat_post/<int:cat_id>', views.suc_category, name='suc_category')
]
