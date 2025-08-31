
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task


@login_required
def index(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        if title:
            Task.objects.create(title=title, user=request.user)
        return redirect("index")

    tasks = Task.objects.filter(user=request.user)
    return render(request, "index.html", {"tasks": tasks})


@login_required
def toggle_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    task.complete = not task.complete
    task.save()
    return redirect("index")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            messages.success(
                request, "Welcome! Your account has been created successfully.")
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
