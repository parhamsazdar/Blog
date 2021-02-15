from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from blog.models import Comments

from blog.serializers import *


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
