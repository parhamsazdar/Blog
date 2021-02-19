import logging

# Create your views here.
from rest_framework import status, generics, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from blog.serializers import *

logger = logging.getLogger(__name__)


class MyCustomUpdateApi(mixins.UpdateModelMixin,
                        GenericAPIView):

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            for user in serializer.validated_data:
                if serializer.validated_data[user][0] == request.user:
                    result = serializer.save()
                    return Response(result)
            else:
                return Response({"error": "فکر کردی زرنگی"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateComment(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentCreateSerializer

    def post(self, request, *args, **kwargs):
        if int(request.data['user']) == request.user.pk:
            return self.create(request, *args, **kwargs)


class EditComment(generics.UpdateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentEdit

    def put(self, request, *args, **kwargs):
        if self.get_object().user == request.user:
            return self.update(request, *args, **kwargs)


class RecordLikePost(MyCustomUpdateApi):
    queryset = Post.objects.all()
    serializer_class = PostLikeSerializer


class RecordDislikePost(MyCustomUpdateApi):
    queryset = Post.objects.all()
    serializer_class = PostDislikeSerializer


class RecordLikeComment(MyCustomUpdateApi):
    queryset = Comments.objects.all()
    serializer_class = CommentLikeSerializer


class RecordDislikeComment(MyCustomUpdateApi):
    queryset = Comments.objects.all()
    serializer_class = CommentDislikeSerializer
