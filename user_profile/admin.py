from django.contrib import admin

from user_profile.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'first_name', 'last_name', 'gender', 'image_profile', 'nickname', 'birth_date',
        'favorite_movie', 'favorite_genre', 'favorite_actor'
    )

    filter_horizontal = ('preferences', )
