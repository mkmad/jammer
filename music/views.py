from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def test(request):
    return render(request, "tests.html", {'test': 'Hey!! this val was passed'})


def profile(request):
    return render(request, "music/profile.html")


def index(request):
    return render(request, "music/index.html")
