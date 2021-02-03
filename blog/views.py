from django.shortcuts import render

# Create your views here.
from blog.forms import Comment
from blog.models import Post, User_info


def test(request,post_id):
    post=Post.objects.get(pk=post_id)
    wirte=User_info.objects.get(user=post.user)
    user_photo=request.user.user.photo
    form=Comment()
    return render(request,"blog/post.html",context={"post":post,"photo":wirte.photo,"user_photo":user_photo,"form":form})
