from django.urls import path
from .views import AddTodo, UpdateTodo, RemoveTodo, TodoList, TodayToDos

urlpatterns = [
    path("add/", AddTodo.as_view(), name="add todo"),
    path("<int:todo_id>/update/", UpdateTodo.as_view(), name="update todo"),
    path("<int:todo_id>/delete/", RemoveTodo.as_view(), name="remove todo"),
    path("list/", TodoList.as_view(), name="todo list"),
    path("today/", TodayToDos.as_view(), name="today todos")

]