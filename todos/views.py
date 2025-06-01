from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from todos.forms import TodoForm
from todos.models import Todo


@login_required(login_url="/users/login/")
def list_todos_view(request):
    uncompleted_todos = Todo.objects.filter(is_completed=False)
    completed_todos = Todo.objects.filter(is_completed=True)
    return render(
        request, "list_todos.html", {"uncompleted_todos": uncompleted_todos, "completed_todos": completed_todos}
    )


@login_required(login_url="/users/login/")
def create_todo_view(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            Todo.objects.create(title=title, user=request.user)
            return redirect('list_todos')
    else:
        form = TodoForm()
    return render(request, "create_todo.html", {"form": form})
