import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.api.serializers import UserRegisterSerializer, UserRetrieveSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        userRetrieve = UserRetrieveSerializer(data=serializer.data)
        userRetrieve.is_valid()

        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
