
from core import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    path("",views.home, name='home'),
    path("userpage/",views.userpage, name='userpage'),

    path("setting/",views.setting, name='setting'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),


]
