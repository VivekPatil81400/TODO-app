from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Todoitems

# Create your views here.

def index(request):
    todo_item = Todoitems.objects.all()
    return render(request, 'todo/index.html', {'all_items': todo_item})

def addTodo(request):
    new_item = Todoitems(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    delete_item = Todoitems.objects.get(id=todo_id)
    delete_item.delete()
    return HttpResponseRedirect('/todo/')