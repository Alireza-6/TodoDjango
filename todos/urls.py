from django.urls import path

from todos.views import list_todos_view, create_todo_view, delete_todo_view, complete_todo_view

urlpatterns = [
    path("", list_todos_view, name="list_todos"),
    path("create-todo/", create_todo_view, name="create_todo"),
    path('delete-todo/<int:todo_id>/', delete_todo_view, name='delete_todo'),
    path('complete-todo/<int:todo_id>/', complete_todo_view, name='complete_todo'),
]
