

from django.urls import path, include

from . import views

app_name = 'api'

urlpatterns = [

    path("create_comment/",views.create_comment,name='create_comment')

]
