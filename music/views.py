from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.views.generic import View, DetailView, ListView

from jammer.forms import UploadFileForm

from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.


class ProfileView(DetailView):
    template_name = 'music/profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'username': request.session['user']})

    def upload_file(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                uploaded_file = request.FILES.keys()[0]
                try:
                    file_ = form.clean_file(uploaded_file)
                except ValidationError as e:
                    return render(request, self.template_name,
                                  {'username': request.session['user'],
                                   'error_message': e.message},)

                self.handle_uploaded_file(file_)
                return render(request, self.template_name,
                              {'username': request.session['user']})
        else:
            return Http404

    def handle_uploaded_file(self, file_):
        pass

    def post(self, request):
        if request.FILES:
            return self.upload_file(request)
        return render(request, self.template_name,
                      {'username': request.session['user']})


class FeedsView(ListView):
    template_name = 'music/feeds.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'username': request.session['user']})


class LocationView(DetailView):
    template_name = 'music/location.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'username': request.session['user']})