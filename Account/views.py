from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class Register(APIView):
    def get(self, request):
        return Response("please enter your user and password")

    def post(self, request):
        user_data = UserSerializers(data=request.data)
        if user_data.is_valid():
            user_data.save()
            return Response(data={"user": user_data.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(data={"error": user_data.errors}, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(
            data={'message': f'Bye {request.user.username}!'},
            status=status.HTTP_204_NO_CONTENT
        )

