from django.urls import path, include

from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index"),
    path('post/<int:pk>', views.PostShow.as_view(), name='post_show'),
    path('cat_post/<int:pk>', views.SubCategoryPost.as_view(), name='suc_category'),
    path('writer_post/<int:pk>', views.WirterPost.as_view(), name="writer_post"),
    path('post_tag/<int:pk>', views.TagsPost.as_view(), name="post_tag"),
    path('log_out/', views.log_out, name='log_out'),
    path('latest_post/', views.LatestPost.as_view(), name="LatestPost"),
    path('popular_post/', views.PopularPost.as_view(), name="PopularPost"),
    path('search_post/',views.search_post,name="search_post"),
    path('search_porefessional/',views.search_porefessional,name="search_porefessional"),
    path('enroll/',views.enroll,name="enroll")

]
