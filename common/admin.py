from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser, UserAdmin)