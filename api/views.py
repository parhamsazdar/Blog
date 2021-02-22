import logging

# Create your views here.
from itertools import chain

from django.http import JsonResponse
from rest_framework import status, generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from blog.models import Word
from blog.serializers import *
from blog.stop_word import stemmer

logger = logging.getLogger(__name__)


class MyCustomUpdateApi(mixins.UpdateModelMixin,
                        GenericAPIView):
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
    queryset = Comments.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EditComment(generics.UpdateAPIView):
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


# class ShowPost(APIView):
#     def post(self, request):
#         serializer = PostSearch(data=request.data)
#         if serializer.is_valid():
#             pass
@api_view(['GET', 'POST'])
def post_search(request):
    if request.method == 'POST':
        serializer = PostSearchIsvalid(data=request.data)
        if serializer.is_valid():
            word = serializer.validated_data["search_word"]
            posts = Post.objects.filter(
                Q(title__contains=word) | Q(user__first_name__contains=word) | Q(user__last_name__contains=word))
            post_serilized = PostSearchShow(posts, many=True)
            return Response(post_serilized.data)
    if request.method == "GET":
        posts = Post.objects.all().defer('id')
        serializer = PostSearchShow(data=posts, many=True)
        if serializer.is_valid():
            return Response(serializer.data)
        return JsonResponse({'ali': 2})


class ShowAllPost(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSearchShow
    model = Post

    def get_queryset(self):
        word = self.request.query_params.get('search_word')
        queryset = self.model.objects.filter(Q(title__contains=word) | Q(user__first_name__contains=word) |
                                             Q(user__last_name__contains=word) | Q(tags__name__contains=word)).distinct(
            'title')
        word_in_text = Word.objects.filter(word=stemmer(word))
        print(word_in_text)
        if len(word_in_text) > 0:
            posts = word_in_text[0].post.all()
            queryset = queryset.union(queryset, posts)
        return queryset
