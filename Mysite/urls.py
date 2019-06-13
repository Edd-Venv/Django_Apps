"""Mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

""" Adding this "path('', include('app_name.urls'))" to the project urlpatterns makes it so that if you go to localhost:8000(home page) 
it matches the path in app_urls(goes to the first app_url"""
# path('', include('todos.urls')),
urlpatterns = [
    path('', include('todos.urls')),
    path('todos/', include('todos.urls')),
    path('admin/', admin.site.urls),
]
