from cgitb import lookup
from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly


class CategroryModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
