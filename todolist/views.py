from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import get_object_or_404
from todolist.forms import TaskForm
from .models import Task
import datetime

# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(
                    reverse("todolist:show_todolist"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                response.set_cookie('username', username)
                return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.filter(user=request.user)
    context = {
        'list_task': data_task,
        'username': request.COOKIES['username'],
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def add_task(request):

    if request.method == "POST":
        form = TaskForm(request.POST)
        try:
            listing = form.save(commit=False)
            listing.user = request.user
            listing.save()

            print('Berhasil nyimpan')
            return HttpResponseRedirect(reverse('todolist:show_todolist'))
        except ValueError as e:
            print(e)
    
    context = {'form': TaskForm()}
    return render(request, 'add_task.html', context)

@login_required(login_url='/todolist/login/')
def delete_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, pk=task_id)
        task.delete()

        return redirect(reverse('todolist:show_todolist'))

@login_required(login_url='/todolist/login/')
def toggle_task_finished(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, pk=task_id)
        task.is_finished = not task.is_finished
        task.save()

        return redirect(reverse('todolist:show_todolist'))
