from django.shortcuts import render, HttpResponse
from .models import ToDo


def homepage(requests):
    return render(requests, "index.html")

def test(requests):
    todo_list = ToDo.objects.all()
    return render(requests, "test.html", {"todo_list": todo_list})

def second(requests):
    return HttpResponse("test 2 page")

def add_todo(requests):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text = text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)
