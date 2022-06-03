from rest_framework.viewsets import ModelViewSet
from comments.models import Comment
from comments.api.serializers import CommentSerializer
from rest_framework.filters import OrderingFilter


class CommentsViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    ordering = ['-created_at']
