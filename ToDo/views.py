from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .serializers import ToDoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
import datetime


class AddTodo(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        todo_serializer = ToDoSerializer(data=request.data)
        if todo_serializer.is_valid():
            todo_serializer.save(user=request.user)
            return Response(data=todo_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=todo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RemoveTodo(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id)
        todo.delete()
        return Response(data={"detail": "The Task is deleted"})


class UpdateTodo(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id)
        new_todo = ToDoSerializer(instance=todo, data=request.data, partial=True)
        if new_todo.is_valid():
            new_todo.save()
            return Response(data=new_todo.data, status=status.HTTP_200_OK)
        else:
            return Response(data=new_todo.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoList(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        todo_list = Todo.objects.get_all_todos_related_to_user(request.user)
        todo_serializer = ToDoSerializer(todo_list, many=True)
        return Response(data=todo_serializer.data, status=status.HTTP_200_OK)


class TodayToDos(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        today_todos = Todo.objects.get_today_todos_related_to_user(user=request.user, date=datetime.date.today())
        todo_serializer = ToDoSerializer(today_todos, many=True)
        return Response(data=todo_serializer.data, status=status.HTTP_200_OK)
