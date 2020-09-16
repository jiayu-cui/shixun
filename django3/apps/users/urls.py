
from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'users'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('login', views.do_login,name='login'),
    path('logout', views.do_logout,name='logout'),
    path('index', views.index,name='index'),
]
