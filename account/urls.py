from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView


urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('login', auth_views.LoginView.as_view(template_name = 'account/login.html',redirect_authenticated_user=True), name="login"),
    path('userlogin', views.login_user, name="login-user"),
    path('logout', views.logoutuser, name="logout"),
]
