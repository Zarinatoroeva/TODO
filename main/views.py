from django.shortcuts import render, HttpResponse

def homepage(requests):
    return HttpResponse("Hello world!")

def test(requests):
    return render(requests, "test.html")
    
