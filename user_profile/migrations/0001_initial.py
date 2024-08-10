# Generated by Django 5.1 on 2024-08-10 13:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_profile', models.ImageField(blank=True, null=True, upload_to='profile_pics')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('nickname', models.CharField(blank=True, max_length=100, null=True)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(max_length=100)),
                ('preferences', models.CharField(max_length=150)),
                ('favorite_movie', models.CharField(blank=True, max_length=200, null=True)),
                ('favorite_genre', models.CharField(blank=True, max_length=50, null=True)),
                ('favorite_actor', models.CharField(blank=True, max_length=300, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
