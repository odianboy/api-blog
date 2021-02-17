from .models import Post, Comment
from rest_framework import serializers


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'author', 'title')


class CommentDetailSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('text', 'author')


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    comments = CommentListSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'

