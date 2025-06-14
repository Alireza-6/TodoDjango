from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

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


@login_required(login_url="/users/login")
def delete_todo_view(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('list_todos')
    return render(request, 'list_todos.html', {'todo': todo})


@login_required(login_url="/users/login/")
def complete_todo_view(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        todo.is_completed = True
        todo.save()
        return redirect('list_todos')
    return render(request, 'list_todos.html', {'todo': todo})
