from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from django.views.generic import CreateView, View
from django.contrib import messages
from django.contrib.auth import login, logout

from user_profile.forms import RegistrationForm, UserProfileForm
from user_profile.models import UserProfile


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


class UserProfileView(LoginRequiredMixin, View):
    model = UserProfile
    template_name = 'user_profile.html'
    form_class = UserProfileForm
    http_method_names = ['get', 'post']
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            profile = UserProfile.objects.create(
                user=request.user, image_profile=form.cleaned_data['image_profile'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                nickname=form.cleaned_data['nickname'],
                birth_date=form.cleaned_data['birth_date'],
                gender=form.cleaned_data['gender'],
                favorite_actor=form.cleaned_data['favorite_actor'],
                favorite_genre=form.cleaned_data['favorite_genre'],
                favorite_movie=form.cleaned_data['favorite_movie'],
            )
            try:
                profile.preferences.set(form.cleaned_data['preferences'])
            except (TypeError, ValueError):
                profile.delete()
            profile.save()
            return HttpResponseRedirect('user_home')
        else:
            messages.info(request, f'{form.errors}')
            return render(request, self.template_name, {'form': self.form_class})


class UserHomeView(View):
    pass


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_message = 'Добро пожаловать на сайт!'
    next_page = 'user_profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация на сайте'
        return context


def logout_user(request):
    logout(request)
    return redirect('login')
