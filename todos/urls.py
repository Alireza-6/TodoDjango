from django.urls import path

from todos.views import list_todos_view, create_todo_view

urlpatterns = [
    path("", list_todos_view, name="list_todos"),
    path("create-todo/", create_todo_view, name="create_todo"),
]
