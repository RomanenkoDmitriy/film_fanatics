from django.urls import path

from user_profile.views import RegisterView, UserProfileView, UserHomeView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('user_profile/', UserProfileView.as_view(), name='user_profile'),
    path('user_home/', UserHomeView.as_view(), name='user_home'),

]