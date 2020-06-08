from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    post_url = serializers.ModelSerializer.serializer_url_field(
        view_name='post_detail')
    author = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Post
        fields = ('title', 'date', 'body', 'author', 'id', 'post_url',)
