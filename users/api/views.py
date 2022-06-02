import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from users.models import User
from users.api.serializers import UserRegisterSerializer, UserRetrieveSerializer, UserUpdateSerializer
from users.models import User


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        userRetrieve = UserRetrieveSerializer(data=serializer.data)
        userRetrieve.is_valid()

        return Response(status=status.HTTP_201_CREATED, data=serializer.data)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserRetrieveSerializer(data=request.user.__dict__)
        serializer.is_valid()
        return Response(serializer.data)

    def put(self, request):
        user = User.objects.get(id=request.user.id)

        serializer = UserUpdateSerializer(user, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)
