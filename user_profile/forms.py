from datetime import datetime

from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from user_profile.models import UserProfile
from film.models import Genre


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


choices_gender = [('Male', 'Male'), ('Female', 'Female')]
query_set_preferences = Genre.objects.all()

year_now = datetime.now().year
years = [i for i in range(year_now - 100, year_now)]


class UserProfileForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=years, empty_label=datetime.now()))
    gender = forms.ChoiceField(choices=choices_gender)
    preferences = forms.ModelMultipleChoiceField(queryset=query_set_preferences, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = UserProfile
        fields = (
            'image_profile', 'first_name', 'last_name', 'nickname', 'birth_date', 'gender', 'preferences',
            'favorite_movie', 'favorite_genre', 'favorite_actor'
        )
