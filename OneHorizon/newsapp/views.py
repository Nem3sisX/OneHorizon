from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def business(request):
    return render(request, "business.html")

def travel(request):
    return render(request, "travel.html")
