from django.contrib.auth import logout, authenticate, login
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render

from main.forms import LoginForm, RegisterForm, AddTodoForm
from main.models import Todo


def index(request):
    if request.user.is_authenticated:
        todos = Todo.objects.filter(author=request.user)
        return render(request, 'main/index.html', {'todos': todos})
    else:
        return redirect(to='login')


def register_view(request):
    if request.user.is_authenticated:
        return redirect(to='home', permanent=True)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to='home')
        else:
            return HttpResponse('Wrong data')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect(to='home', permanent=True)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(to='home')
                else:
                    return HttpResponse("User is not activated")
            else:
                return HttpResponse('Wrong data')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect(to='home', permanent=True)
    logout(request)
    return redirect(to='home')


def add_todo(request):
    if not request.user.is_authenticated:
        return redirect(to='home', permanent=True)
    if request.method == 'POST':
        form = AddTodoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(author=request.user, content=cd['content'])
            return redirect(to='home')
        else:
            return HttpResponse('Wrong data')
    else:
        form = AddTodoForm()

    return render(request, 'main/add_todo.html', {'form': form})


def remove_todo(request, todo_id):
    Todo.objects.get(pk=todo_id).delete()
    return redirect(to='home')
