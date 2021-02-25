import logging
from rest_framework import status, generics, mixins, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.db.models import Q

from blog.models import Word
from blog.serializers import *
from blog.stop_word import stemmer

logger = logging.getLogger(__name__)


class MyCustomUpdateApi(mixins.UpdateModelMixin,
                        GenericAPIView):
    """
    In this class we check if the the user is like or dislike a post or comment is
    request.user and validation of the serializer here is available in put method from this
    class
    This class is also for update a model instance. I mean update like or dislike a post or comment
    """
    permission_classes = [permissions.IsAuthenticated]

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
    """
    This class is also for creating comment for specific user

    """
    queryset = Comments.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EditComment(generics.UpdateAPIView):
    """
    This class is for editing comment and checked request.user == user who requested
    from the client

    """
    queryset = Comments.objects.all()
    serializer_class = CommentEdit
    permission_classes = [permissions.IsAuthenticated]

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


class ShowAllPost(generics.ListAPIView):
    """
    This class receive query pram with method get that i named it search word.
    I use search word for searching in my database. But the point is search word can
    appear in title or text or tags or ... of the post.
    I use this APIView for live ajax for simple search in menubar of my site.
    """
    queryset = Post.objects.all()
    serializer_class = PostSearchShow
    model = Post

    def get_queryset(self):
        # Query param cant be empty.I Handle this in my java script Code.
        word = self.request.query_params.get('search_word')
        queryset = self.model.objects.filter(confirm=True, active=True).filter(
            Q(title__contains=word) | Q(user__first_name__contains=word) |
            Q(user__last_name__contains=word) | Q(category__name__contains=word) | Q(
                tags__name__contains=word)).distinct(
            'title')
        # Here I check if the search word exist in my Word model.
        word_in_text = Word.objects.filter(word=stemmer(word))
        if len(word_in_text) > 0:
            posts = word_in_text[0].post.filter(confirm=True, active=True)
            # For best performance I union between queryset and posts
            queryset = queryset.union(queryset, posts)
        return queryset[:5]
