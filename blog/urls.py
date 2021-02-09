from django.urls import path, include

from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index"),
    path("test/",views.test,name="test"),
    path("test_2/", views.test_2, name="test_2"),
    path('post/<int:post_id>', views.post_show, name='post_show')
]
