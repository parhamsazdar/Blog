from django.urls import path, include

from . import views

app_name = 'api'

urlpatterns = [

    path("create_comment/", views.create_comment, name='create_comment'),
    path("record_like_post/<int:post_id>", views.record_like_post, name='record_like_post'),
    path("record_dislike_post/<int:post_id>", views.record_dislike_post, name='record_dislike_post'),
    path("record_dislike_comment/<int:comment_id>", views.record_dislike_comment, name='record_dislike_comment'),
    path("record_like_comment/<int:comment_id>", views.record_like_comment, name='record_like_comment'),
    path("edit_comment/<int:comment_id>",views.edit_comment,name="edit_comment")
]
