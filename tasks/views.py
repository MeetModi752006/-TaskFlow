from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count
from django.utils import timezone
from .models import Task, Category
from .forms import TaskForm, CategoryForm


@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    today = timezone.now().date()

    stats = {
        'total': tasks.count(),
        'todo': tasks.filter(status='todo').count(),
        'in_progress': tasks.filter(status='in_progress').count(),
        'completed': tasks.filter(status='completed').count(),
        'overdue': tasks.filter(due_date__lt=today, status__in=['todo', 'in_progress']).count(),
        'starred': tasks.filter(is_starred=True).count(),
        'urgent': tasks.filter(priority='urgent', status__in=['todo', 'in_progress']).count(),
    }

    recent_tasks = tasks.exclude(status='completed').order_by('-is_starred', 'due_date', '-created_at')[:8]
    categories = Category.objects.filter(user=request.user).annotate(task_count=Count('tasks'))

    context = {
        'stats': stats,
        'recent_tasks': recent_tasks,
        'categories': categories,
        'today': today,
        'page': 'dashboard',
    }
    return render(request, 'tasks/dashboard.html', context)


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    today = timezone.now().date()

    # Filters
    status_filter = request.GET.get('status', '')
    priority_filter = request.GET.get('priority', '')
    category_filter = request.GET.get('category', '')
    search_query = request.GET.get('q', '')
    sort_by = request.GET.get('sort', '-created_at')
    starred_filter = request.GET.get('starred', '')

    if status_filter:
        tasks = tasks.filter(status=status_filter)
    if priority_filter:
        tasks = tasks.filter(priority=priority_filter)
    if category_filter:
        tasks = tasks.filter(category_id=category_filter)
    if search_query:
        tasks = tasks.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    if starred_filter:
        tasks = tasks.filter(is_starred=True)

    valid_sorts = ['created_at', '-created_at', 'due_date', '-due_date', 'title', '-title', 'priority']
    if sort_by not in valid_sorts:
        sort_by = '-created_at'
    tasks = tasks.order_by(sort_by)

    categories = Category.objects.filter(user=request.user)

    context = {
        'tasks': tasks,
        'categories': categories,
        'today': today,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
        'category_filter': category_filter,
        'search_query': search_query,
        'sort_by': sort_by,
        'starred_filter': starred_filter,
        'page': 'tasks',
    }
    return render(request, 'tasks/task_list.html', context)


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.user, request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, f'Task "{task.title}" created successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(request.user)

    return render(request, 'tasks/task_form.html', {
        'form': form,
        'action': 'Create',
        'page': 'tasks',
    })


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    today = timezone.now().date()
    return render(request, 'tasks/task_detail.html', {
        'task': task,
        'today': today,
        'page': 'tasks',
    })


@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.user, request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, f'Task "{task.title}" updated successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(request.user, instance=task)

    return render(request, 'tasks/task_form.html', {
        'form': form,
        'task': task,
        'action': 'Update',
        'page': 'tasks',
    })


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        title = task.title
        task.delete()
        messages.success(request, f'Task "{title}" deleted successfully!')
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task, 'page': 'tasks'})


@login_required
def task_toggle_status(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if task.status == 'completed':
        task.status = 'todo'
    else:
        task.status = 'completed'
    task.save()
    messages.success(request, f'Task marked as {task.get_status_display()}!')
    return redirect(request.META.get('HTTP_REFERER', 'task_list'))


@login_required
def task_toggle_star(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_starred = not task.is_starred
    task.save()
    return redirect(request.META.get('HTTP_REFERER', 'task_list'))


@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user).annotate(task_count=Count('tasks'))
    return render(request, 'tasks/category_list.html', {
        'categories': categories,
        'page': 'categories',
    })


@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.user = request.user
            cat.save()
            messages.success(request, f'Category "{cat.name}" created!')
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'tasks/category_form.html', {
        'form': form,
        'action': 'Create',
        'page': 'categories',
    })


@login_required
def category_edit(request, pk):
    cat = get_object_or_404(Category, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            messages.success(request, f'Category updated!')
            return redirect('category_list')
    else:
        form = CategoryForm(instance=cat)
    return render(request, 'tasks/category_form.html', {
        'form': form,
        'category': cat,
        'action': 'Update',
        'page': 'categories',
    })


@login_required
def category_delete(request, pk):
    cat = get_object_or_404(Category, pk=pk, user=request.user)
    if request.method == 'POST':
        name = cat.name
        cat.delete()
        messages.success(request, f'Category "{name}" deleted!')
        return redirect('category_list')
    return render(request, 'tasks/category_confirm_delete.html', {'category': cat, 'page': 'categories'})
