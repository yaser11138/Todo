from django.urls import path
from .views import AddTodo, UpdateTodo, RemoveTodo

urlpatterns = [
    path("add/", AddTodo, name="addtodo"),
    path("<int:todo_id>/update/", UpdateTodo, name="updatetodo"),
    path("<int:todo_id>/delete/", RemoveTodo,name="removetodo")

]