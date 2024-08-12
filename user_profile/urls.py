from django.contrib.auth.views import LoginView
from django.urls import path

from user_profile.views import RegisterView, UserProfileView, UserLoginView, logout_user

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('user_profile/', UserProfileView.as_view(), name='user_profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),

]