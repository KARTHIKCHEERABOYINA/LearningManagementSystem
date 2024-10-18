from django.shortcuts import render, redirect
from .models import Task, Solution
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def home(request):
    tasks = Task.objects.all()
    return render(request, 'main/home.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        difficulty = request.POST['difficulty']
        task = Task(title=title, description=description, difficulty=difficulty, created_by=request.user)
        task.save()
        return redirect('home')
    return render(request, 'main/add_task.html')

@login_required
def add_solution(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        solution_code = request.POST['solution_code']
        explanation = request.POST['explanation']
        complexity = request.POST['complexity']
        solution = Solution(task=task, solution_code=solution_code, explanation=explanation, complexity=complexity, submitted_by=request.user)
        solution.save()
        return redirect('home')
    return render(request, 'main/add_solution.html', {'task': task})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})
