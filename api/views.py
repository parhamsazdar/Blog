import logging
from json import load, dump, dumps

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from blog.models import Comments

from blog.serializers import *

logger = logging.getLogger(__name__)


@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer])
def create_comment(request):
    """
    create comment for specific user and specific post.
    """

    if request.method == 'GET':
        comments = Comments.objects.all()
        serializer = CommentCreateSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer])
def record_like_post(request, post_id):
    """
    create like for specific user and specific post.
    """
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        logger.error('get')
        post_like = Post.objects.all()
        serializer = PostLikeSerializer(post_like, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        logger.error('post')
        serializer = PostLikeSerializer(post, data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            return JsonResponse(result)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer])
def record_dislike_post(request, post_id):
    """
    create dislike for specific user and specific post.
    """
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        post_dislike = Post.objects.all()
        serializer = PostDislikeSerializer(post_dislike, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostDislikeSerializer(post, data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            return JsonResponse(result)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer])
def record_like_comment(request, comment_id):
    """
    create like for specific user and specific comment.
    """
    try:
        comment = Comments.objects.get(id=comment_id)
    except Comments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        logger.error('get')
        comment_like = Comments.objects.all()
        serializer = CommentLikeSerializer(comment_like, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        logger.error('post')
        serializer = CommentLikeSerializer(comment, data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            return JsonResponse(result)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer])
def record_dislike_comment(request, comment_id):
    """
    create dislike for specific user and specific comment.
    """
    try:
        comment = Comments.objects.get(id=comment_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        comment_dislike = Comments.objects.all()
        serializer = CommentDislikeSerializer(comment_dislike, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentDislikeSerializer(comment, data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            return JsonResponse(result)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
