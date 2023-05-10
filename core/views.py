from django.shortcuts import render, redirect
from .models import User
from .forms import userForm

def index(request):
    user = User.objects.first()
    context = {'user': user}
    return render(request, 'core/index.html', context)

def edit(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method != 'POST':
        form = userForm(instance=user)
    else:
        form = userForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('core:index')
    context = {'form': form,'user': user}
    return render(request, 'core/edit.html', context)

def new_user(request):
    if request.method != 'POST':
        form = userForm()
    else:
        user = User.objects.first()
        form = userForm(data=request.POST)
        if form.is_valid():
            form.save()
            context = {'user': user}
            return redirect('core:index')
    context = {'form': form}
    return render(request, 'core/new_user.html', context)

def list(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'core/list.html', context)