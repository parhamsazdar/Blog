from django.urls import path, include

from . import views

app_name = 'api'

urlpatterns = [

    path("record_like_post/<int:pk>", views.RecordLikePost.as_view(), name='record_like_post'),
    path("record_dislike_post/<int:pk>", views.RecordDislikePost.as_view(), name='record_dislike_post'),
    path("record_dislike_comment/<int:pk>", views.RecordDislikeComment.as_view(), name='record_dislike_comment'),
    path("record_like_comment/<int:pk>", views.RecordLikeComment.as_view(), name='record_like_comment'),
    path("create_comment/", views.CreateComment.as_view(), name="create_comment"),
    path("edit_comment/<int:pk>", views.EditComment.as_view(), name="edit_comment"),
    path("post_all/", views.ShowAllPost.as_view(), name="show_all_post"),

]
