from django.shortcuts import render


def list_todos_view(request):
    return render(request, "list_todos.html")
