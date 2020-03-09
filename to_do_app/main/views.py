from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by('-added_date')
    items_html = {
        "todo_items": todo_items
    }
    return render(request, 'main/index.html', items_html)

@csrf_exempt
def add_todo(request):
    added_date = timezone.now()
    content = request.POST["content"]
    created_object = Todo.objects.create(added_date=added_date, text=content)
    print(created_object)
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
