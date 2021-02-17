from django.urls import path, include

from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index"),
    path('post/<int:post_id>', views.post_show, name='post_show'),
    path('cat_post/<int:cat_id>', views.suc_category, name='suc_category'),
    path('writer_post/<int:writer_id>', views.writer_post, name="writer_post"),
    path('post_tag/<int:tag_id>', views.post_tag, name="post_tag"),
    path('log_out/', views.log_out, name='log_out'),
    path('latest_post/', views.LatestPost.as_view(), name="LatestPost"),
    path('popular_post/', views.PopularPost.as_view(), name="PopularPost")
]
