from django.shortcuts import render
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
        return render(request, 'core/index.html', {'user': user})
    context = {'form': form,'user': user}
    return render(request, 'core/edit.html', context)
