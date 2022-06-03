from rest_framework.permissions import BasePermission
from comments.models import Comment


class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            id_comment = view.kwargs['pk']
            comment = Comment.objects.get(pk=id_comment)

            print(f"Comment User id: {comment.user_id}")
            print(f"Actual User id: {request.user.pk}")

            id_user = request.user.pk
            return id_user == comment.user_id
