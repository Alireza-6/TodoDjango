from django.urls import path

from todos.views import list_todos_view

urlpatterns = [
    path("", list_todos_view, name="list_todos")
]
