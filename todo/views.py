from django.shortcuts import render, redirect
from .models import Item
# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items':items
    }
    return render(request, 'todo/todo_app.html', context)


def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('todo/todo_app.html')
    return render(request, 'todo/add_item.html')


