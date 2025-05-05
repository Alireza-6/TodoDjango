from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from users.forms import CustomUserCreationForm
from users.models import CustomUser


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = CustomUser.objects.create_user(email=email, password=password)
            login(request, user)
            return redirect("list_todos")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("list_todos")
    return render(request, "login.html")
