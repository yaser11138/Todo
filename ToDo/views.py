from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .serializers import ToDoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Todo


class AddTodo(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        todo = ToDoSerializer(data=request.data)
        if todo.is_valid():
            todo = todo.save()
            Response(data=todo.data, status=status.HTTP_201_CREATED)
        else:
            Response(data=todo.errors, status=status.HTTP_400_BAD_REQUEST)


class RemoveTodo(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id)
        todo.delete()
        Response(data={"detail": "The Task is deleted"})


class UpdateTodo(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id)
        new_todo = ToDoSerializer(instance=Todo,data=request.data,partial=True)
        if new_todo.is_valid():
            todo.save()
            return Response(data=new_todo.data, status=status.HTTP_200_OK)
        else:
            return Response(data=new_todo.errors, status=status.HTTP_400_BAD_REQUEST)




