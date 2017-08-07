from django.shortcuts import render
from django.views.generic import View, DetailView, ListView

from django.http import HttpResponse

# Create your views here.


def test(request):
    return render(request, "tests.html", {'test': 'Hey!! this val was passed'})


class ProfileView(DetailView):
    template_name = 'music/profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'username': request.session['user']})


class FeedsView(ListView):
    template_name = 'music/feeds.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'username': request.session['user']})


class LocationView(DetailView):
    template_name = 'music/location.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'username': request.session['user']})