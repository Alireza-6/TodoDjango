from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from todos.models import Todo


@login_required(login_url="/users/login/")
def list_todos_view(request):
    uncompleted_todos = Todo.objects.filter(is_completed=False)
    completed_todos = Todo.objects.filter(is_completed=True)
    return render(
        request, "list_todos.html", {"uncompleted_todos": uncompleted_todos, "completed_todos": completed_todos}
    )
