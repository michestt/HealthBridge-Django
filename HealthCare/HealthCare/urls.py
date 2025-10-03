"""HealthCare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from .views import homepage, like, LoginPage, LogOutPage, RegisterPage

urlpatterns = [
    path('login/<str:page>', LoginPage),
    path('login/', LoginPage, name='login'),
    path('login/post_homepage', LoginPage, name='login/post_homepage'),
    path('login/blog_homepage', LoginPage, name='login/blog_homepage'),
    path('login/blog_show_my_posts', LoginPage, name='login/blog_show_my_posts'),
    path('login/blog_weight_lost', LoginPage, name='login/blog_weight_lost'),
    path('login/blog_sport', LoginPage, name='login/blog_sport'),
    path('login/home', LoginPage, name='login/home'),
    #####################################################################
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('home_like/<slug:slug>/', like, name='postlike_home'),
    path('logout/', LogOutPage, name='logout'),
    path('register/', RegisterPage, name='register'),
    path('calories/', include('calories.urls')),
    url(r'myblog/', include('blog.urls')),
    url(r'^recipe/', include('recipe.urls')),
    url(r'^fitforum/', include('fitforum.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^discuss/', include('Discussion_forum.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^profile/', include('healthprofile.urls')),


] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
