from django.shortcuts import render, HttpResponse
from .models import ToDo


def homepage(requests):
    return render(requests, "index.html")

def test(requests):
    todo_list = ToDo.objects.all()
    return render(requests, "test.html", {"todo_list": todo_list})

def second(requests):
    return HttpResponse("test 2 page")

def third(requests):
    return HttpResponse("This is page test 3")
    
