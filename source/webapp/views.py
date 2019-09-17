
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
        if not form.is_valid():
            return render(request, 'create.html', context={'form': form})

        plan = ToDoList.objects.create(
            description=form.cleaned_data['description'],
            status=form.cleaned_data['status'],
            text=form.cleaned_data['text'],
            done_at=form.cleaned_data['done_at'])
        return redirect('plan_view', pk=plan.pk)


def plan_update_view(request, pk):
    plan = get_object_or_404(ToDoList, pk=pk)
    if request.method == 'GET':
        form = PlanForm(data={
            'description': plan.description,
            'text': plan.text,
            'status': plan.status,
            'done_at': plan.done_at
        })
        return render(request, 'update.html', context={
            'plan': plan,
            'form': form
        })
    elif request.method == 'POST':
        form = PlanForm(data=request.POST)
        if form.is_valid():
            plan.description = form.cleaned_data['description']
            plan.status = form.cleaned_data['status']
            plan.done_at = form.cleaned_data['done_at']
            plan.text = form.cleaned_data['text']
            plan.save()
            return redirect('plan_view', pk=plan.pk)
        else:
            return render(request, 'create.html', context={
                'form': form,
                'plan': plan
            })


def plan_delete_view(request, pk):
    plan = get_object_or_404(ToDoList, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'plan': plan})
    elif request.method == 'POST':
        plan.delete()
        return redirect('index')