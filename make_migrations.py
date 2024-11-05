#!/usr/bin/env python

# Django
import django
from django.conf import settings
from django.core.management import call_command

settings.configure(
    DEBUG=True,
    INSTALLED_APPS=(
        "django.contrib.contenttypes",
        "django.contrib.auth",
        "daily_active_users.apps.DailyActiveUsersConfig",
    ),
)

django.setup()
call_command("makemigrations", "daily_active_users")
