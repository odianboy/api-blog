from .models import Post
from rest_framework import generics
from .serializers import PostDetailSerializer, PostListSerializer, CommentDetailSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostDetailSerializer


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated, )


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentDetailSerializer
