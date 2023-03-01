import os

def apps():
     return [
        # Applications perso ajoutés
        'maintenance.apps.MaintenanceConfig',
        'polls.apps.PollsConfig',
        'news.apps.NewsConfig',
        'users.apps.UsersConfig',

        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]