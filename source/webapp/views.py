
from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import ToDoList, STATUS_CHOICES
from webapp.forms import PlanForm


def index_view(request, *args, **kwargs):
    plans = ToDoList.objects.all()
    return render(request, 'index.html', context={
        'plans': plans
    })

def plans_view(request, pk):
    plan = get_object_or_404(ToDoList, pk=pk)
    return render(request, 'plans.html', context={
        'plan': plan
    })

def plan_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = PlanForm()
        return render(request, 'create.html', context={
            'status_choices': STATUS_CHOICES,
            'form': form
        })
    elif request.method == 'POST':
        form = PlanForm(data=request.POST)
        date = request.POST.get('time')
        if date == '':
            date = None
        if not form.is_valid():
            return render(request, 'create.html', context={'form': form})

        plan = ToDoList.objects.create(
            description=form.cleaned_data['description'],
            status=form.cleaned_data['status'],
            text=form.cleaned_data['text'])
        return redirect('plan_view', pk=plan.pk)


def plan_update_view(request, pk):
    plan = get_object_or_404(ToDoList, pk=pk)
    if request.method == 'GET':
        return render(request, 'update.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        plan.description = request.POST.get('description')
        plan.status = request.POST.get('status')
        plan.date = request.POST.get('time')
        plan.text = request.POST.get('text')
        if plan.date == '':
            plan.date = None
        plan.save()
        return redirect('plan_view', pk=plan.pk)


def plan_delete_view(request, pk):
    plan = get_object_or_404(ToDoList, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'plan': plan})
    elif request.method == 'POST':
        plan.delete()
        return redirect('index')