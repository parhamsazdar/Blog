from rest_framework import serializers

from blog.models import Post, Comments


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

