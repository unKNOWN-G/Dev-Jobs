"""devjobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url, include
from app import views

urlpatterns = [
    url(r'^app/',include("app.urls")),
    path('admin/', admin.site.urls),
    url(r'^register/',views.user_register,name = 'register' ),
    url(r'^job/',views.job_register,name = 'job' ),
    url(r'^login/',views.user_login,name = 'login' ),
    url(r'^invalid/',views.invalid,name = 'invalid' ),
    url(r'^logout/',views.user_logout,name = 'logout' ),
    url(r'^dashboard/',views.special,name = 'dashboard' ),
    url(r'^',views.home,name = 'home' ),

]
