from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import TaskForm
from webapp.models import Task


def index_view(request, *args, **kwargs):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={
        'tasks': tasks
    })


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={'task': task})


def task_create_view(request, *args, **kwargs):
    if request.method == 'GET':

        form = TaskForm()

        return render(request, 'create.html', context={'form': form})

    elif request.method == 'POST':

        form = TaskForm(data=request.POST)

        if form.is_valid():

            article = Task.objects.create(

                description=form.cleaned_data['description'],

                date=form.cleaned_data['date'],

                text=form.cleaned_data['text'],

                status=form.cleaned_data['status']

            )

            return redirect('task_view', pk=article.pk)

        else:

            return render(request, 'create.html', context={'form': form})


def task_update_view(request, pk):

    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(data=request.POST)

    if request.method == 'GET':
        form = TaskForm(data={
            'description': task.description,
            'text': task.text,
            'status': task.status,
            'date': task.date
        })
        return render(request, 'update.html', context={'task': task, 'form': form})

    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data['description']
            task.date = form.cleaned_data['date']
            task.status = form.cleaned_data['status']
            task.text = form.cleaned_data['text']
            task.save()
            return redirect('task_view', pk=task.pk)


def task_delete_view(request, pk):

    task = get_object_or_404(Task, pk=pk)

    if request.method == 'GET':

        return render(request, 'delete.html', context={'task': task})

    elif request.method == 'POST':

        task.delete()

        return redirect('index')


def task_delete_check_view(request):
    if request.method == 'POST':
        delete = request.POST.getlist('delete')
        for check in delete:
            task = get_object_or_404(Task, pk=check)
            task.delete()
        return redirect('index')