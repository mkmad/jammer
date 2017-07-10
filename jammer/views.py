from django.shortcuts import render, HttpResponse

from django.views.generic import View, DetailView, ListView
from .forms import UserForm

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.


def index(request):
    return render(request, "base.html")

# Create a registration view from a generic view
# class.


class FeedsView(ListView):
    template_name = 'music/feeds.html'


class ProfileView(DetailView):
    template_name = 'music/profile.html'


class RegistrationView(View):
    # template_name = 'registration/registration.html'
    def get(self, request):
        return render(request, 'registration/registration.html')

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # I dont need these as I am not going to use
            # these fields here:

            # firstname = form.cleaned_data['firstname']
            # lastname = form.cleaned_data['lastname']

            # Password needs to be set like this.
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            username = form.cleaned_data['username']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'music/index.html', {'user': user})
        context = {
            "form": form,
            "error_message": form.errors
        }
        return render(request, 'registration/registration.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        form = UserForm(request.POST or None)
        context = {
            "form": form,
        }
        return render(request, 'registration/login.html', context)


class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'music/index.html', {'username': username})
            else:
                return render(request, 'registration/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'registration/login.html', {'error_message': 'Invalid login'})

    def get(self, request):
        return render(request, 'registration/login.html')

