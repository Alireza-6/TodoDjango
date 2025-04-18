from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="/users/login/")
def list_todos_view(request):
    return render(request, "list_todos.html")
