from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Post, Comments


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ["text", "user", "post"]


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ["id", "user"]


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "like"]
