# #Function based view
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Task
#
# # List all tasks with search functionality
# def task_list(request):
#     query = request.GET.get('q')  # Get the search query
#     if query:
#         tasks = Task.objects.filter(title__icontains=query) | Task.objects.filter(description__icontains=query)
#     else:
#         tasks = Task.objects.all()
#     return render(request, 'task_list.html', {'tasks': tasks})
#
# # Create a new task
# def task_create(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         due_date = request.POST.get('due_date')
#         status = request.POST.get('status')
#         Task.objects.create(title=title, description=description, due_date=due_date, status=status)
#         return redirect('task_list')
#     return render(request, 'task_create.html')
#
# # Update an existing task
# def task_update(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     if request.method == 'POST':
#         task.title = request.POST.get('title')
#         task.description = request.POST.get('description')
#         task.due_date = request.POST.get('due_date')
#         task.status = request.POST.get('status')
#         task.save()
#         return redirect('task_list')
#     return render(request, 'task_update.html', {'task': task})
#
# # Delete a task
# def task_delete(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     if request.method == 'POST':
#         task.delete()
#         return redirect('task_list')
#     return render(request, 'task_confirm_delete.html', {'task': task})

#Class based view
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

# List all tasks with search functionality
class TaskListView(View):
    def get(self, request):
        query = request.GET.get('q')  # Get the search query
        if query:
            tasks = Task.objects.filter(title__icontains=query) | Task.objects.filter(description__icontains=query)
        else:
            tasks = Task.objects.all()
        return render(request, 'task_list.html', {'tasks': tasks})

# Create a new task
class TaskCreateView(View):
    def get(self, request):
        return render(request, 'task_create.html')

    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        status = request.POST.get('status')
        Task.objects.create(title=title, description=description, due_date=due_date, status=status)
        return redirect('task_list')

# Update an existing task
class TaskUpdateView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task_update.html', {'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.status = request.POST.get('status')
        task.save()
        return redirect('task_list')

# Delete a task
class TaskDeleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task_confirm_delete.html', {'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('task_list')
