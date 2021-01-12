from django.shortcuts import render, HttpResponse

def homepage(requests):
    return HttpResponse("Hello world!")

def test(requests):
    return render(requests, "test.html")

def second(requests):
    return HttpResponse("test 2 page")

def third(requests):
    return HttpResponse("This is page test 3")
    
