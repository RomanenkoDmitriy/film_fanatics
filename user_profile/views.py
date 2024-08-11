from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User
from django.views.generic import CreateView, View
from django.contrib import messages
from django.contrib.auth import login

from user_profile.forms import RegistrationForm


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    model = User
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
            )
            login(request, user)
            return HttpResponseRedirect('user_profile')

        else:
            messages.info(request, f'{form.errors}')
            return render(request, self.template_name, {'form': self.form_class})


class UserProfileView(View):
    pass
