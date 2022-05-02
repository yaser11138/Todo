from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializers


class Register(APIView):
    def get(self, request):
        return Response("please enter your user and password")

    def post(self, request):
        user_data = UserSerializers(data=request.data)
        if user_data.is_valid():
            user_data.save()
            return Response(data={"user": user_data.data})
        else:
            return Response(data={"error": user_data.errors})


