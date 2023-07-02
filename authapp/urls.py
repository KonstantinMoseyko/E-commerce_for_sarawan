from django.urls import path

import authapp.views as authapp
from authapp.apps import AuthappConfig

app_name = AuthappConfig.name

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('register/', authapp.register, name='register'),
]