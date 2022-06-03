from rest_framework import serializers
from posts.models import Post
from users.api.serializers import UserRetrieveSerializer
from categories.api.serializers import CategorySerializer


class PostSerializer(serializers.ModelSerializer):
    user_data = UserRetrieveSerializer(source='user', read_only=True)
    category_data = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'slug', 'miniature',
                  'created_at', 'updated_at', 'published', 'user', 'category', 'user_data', 'category_data')
