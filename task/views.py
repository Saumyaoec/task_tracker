from django.shortcuts import render
from task.models import Task
from task.forms import TaskForm

from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.


class TaskListHomeView(View):
    template_name = 'task_list.html'

    def get(self, request):
        tasks = Task.objects.all()
        return render(request, self.template_name,{'tasks': tasks})


class TaskAddView(View):
    template_name = 'add_task.html'

    def get(self, request):
        form = TaskForm()
        return render(request, self.template_name,{'form': form})
    def post(self,request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, self.template_name,{'form':form})

class TaskUpdateView(View):
    template_name = 'update_task.html'

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
        return render(request, self.template_name,{'form':form, 'task': task})
    
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, self.template_name, {'form':form, 'task': task})

class TaskDeleteView(View):
    template_name = 'delete_task.html'

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, self.template_name,{'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('task_list')

