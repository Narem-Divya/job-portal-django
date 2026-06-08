from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('list/', views.jobs),
    path('apply/', views.apply_job),
    path('register/', views.register),
    path('login/', views.login_user),
    path('logout/', views.logout_user),
]