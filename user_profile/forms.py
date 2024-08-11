from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput())
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repeat the password', widget=forms.PasswordInput())
    usable_password = None

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        clean_data = self.cleaned_data
        if clean_data['password1'] != clean_data['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return clean_data['password2']




