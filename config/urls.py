"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from login.views import login_view, login_user
from homepage.views import Homepage, logout
from register.views import register, create_register
from upload_file.views import subida_archivos, save_result
from delete_history.views import History, eliminar_registro
from show_result.views import Show_Results

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Homepage, name='home'),
    path('loginusers/', login_view, name='login'),
    path('registerusers/', register, name='register'),
    path('upload-file/', subida_archivos, name='uptoload-file'),
    path('delete-history/', History, name='delete-history'),
    path('show-result/', Show_Results, name='show-result'),
    path('save_result/', save_result, name='save_result'),
    path('create-user/', create_register, name='create_user'),
    path('login_user/', login_user, name='login_user'),
    path('eliminar_registro/<int:registro_id>/', eliminar_registro, name='eliminar_registro'),
    path('logout/', logout, name='logout'),
]
