from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.views.generic import View, DetailView, ListView

from jammer.forms import UploadFileForm
from .models import UserProfile
from django.conf import settings

from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.


class ProfileView(DetailView):
    template_name = 'music/profile.html'

    def get(self, request, *args, **kwargs):
        if UserProfile.objects.filter(user=request.user.id).exists():
            inst = UserProfile.objects.get(user=request.user.id)
            return self.render_content(request, inst)
        return render(request, self.template_name, {
            'username': request.session['user']})

    def render_content(self, request, inst):
        if inst.profile_pic and inst.background_pic:
            return render(request, self.template_name,
                          {'username': request.session['user'],
                           'profile_pic': inst.profile_pic.url,
                           'background_pic': inst.background_pic.url})
        elif inst.background_pic:
            return render(request, self.template_name,
                          {'username': request.session['user'],
                           'background_pic': inst.background_pic.url})
        elif inst.profile_pic:
            return render(request, self.template_name,
                          {'username': request.session['user'],
                           'profile_pic': inst.profile_pic.url})

    def upload_file(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            # TODO (mohan): Validate form correctly!
            if form.is_valid():
                uploaded_file_type = request.FILES.keys()[0]
                try:
                    file_ = form.clean_file(uploaded_file_type)
                    inst = self.handle_uploaded_file(uploaded_file_type, file_,
                                                     request.user)
                except ValidationError as e:
                    return render(request, self.template_name,
                                  {'username': request.session['user'],
                                   'error_message': e.message},)
                except Exception as ex:
                    return render(request, self.template_name,
                                  {'username': request.session['user'],
                                   'error_messages': ex.message},)
                else:
                    return self.render_content(request, inst)

    @staticmethod
    def handle_uploaded_file(file_type, file_, user):

        if file_type == 'background_pic_form':
            if UserProfile.objects.filter(user=user.id).exists():
                inst = UserProfile.objects.get(user=user.id)
                inst.background_pic = file_
                inst.save()
            else:
                inst = UserProfile(user=user, background_pic=file_)
                inst.save()

            return inst

        elif file_type == 'profile_pic_form':
            if UserProfile.objects.filter(user=user.id).exists():
                inst = UserProfile.objects.get(user=user.id)
                inst.profile_pic = file_
                inst.save()
            else:
                inst = UserProfile(user=user, profile_pic=file_)
                inst.save()

            return inst
        else:
            raise Exception('Invalid File Type')

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