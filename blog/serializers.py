from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Post, Comments





class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["like"]

    def update(self, instance, validated_data):
        like = validated_data.pop('like')
        if like[0] not in instance.like.all():
            if like[0] not in instance.dislike.all():
                instance.like.add(like[0])
                return {'result': "شما این پست را پسندیدید", "status": 200}
            else:
                instance.dislike.remove(like[0])
                instance.like.add(like[0])
                return {'result': "شما این پست را پسندیدید", "status": 201}
        else:
            instance.like.remove(like[0])
            return {'result': "شما بازخورد مثبت خود را نسبت به پست برداشتید", "status": 202}


class PostDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["dislike"]

    def update(self, instance, validated_data):
        dislike = validated_data.pop('dislike')
        if dislike[0] not in instance.dislike.all():
            if dislike[0] not in instance.like.all():
                instance.dislike.add(dislike[0])
                return {'result': "شما این پست را نمی پسندیدید", "status": 200}
            else:
                instance.like.remove(dislike[0])
                instance.dislike.add(dislike[0])
                return {'result': "شما این پست را نمی پسندیدید", "status": 201}
        else:
            instance.dislike.remove(dislike[0])
            return {'result': "شما بازخورد منفی خود را نسبت به پست برداشتید", "status": 202}




class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ["text", "user", "post"]




class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ["like"]

    def update(self, instance, validated_data):
        like = validated_data.pop('like')
        if like[0] not in instance.like.all():
            if like[0] not in instance.dislike.all():
                instance.like.add(like[0])
                return {'result': "شما این نظر را پسندیدید", "status": 200}
            else:
                instance.dislike.remove(like[0])
                instance.like.add(like[0])
                return {'result': "شما این نظر را پسندیدید", "status": 201}
        else:
            instance.like.remove(like[0])
            return {'result': "شما بازخورد مثبت خود را نسبت به نظر برداشتید", "status": 202}


class CommentDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ["dislike"]

    def update(self, instance, validated_data):
        dislike = validated_data.pop('dislike')
        if dislike[0] not in instance.dislike.all():
            if dislike[0] not in instance.like.all():
                instance.dislike.add(dislike[0])
                return {'result': "شما این نظر را نمی پسندیدید", "status": 200}
            else:
                instance.like.remove(dislike[0])
                instance.dislike.add(dislike[0])
                return {'result': "شما این نظر را نمی پسندیدید", "status": 201}
        else:
            instance.dislike.remove(dislike[0])
            return {'result': "شما بازخورد منفی خود را نسبت به نظر برداشتید", "status": 202}


class CommentEdit(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ["text","confirm"]
