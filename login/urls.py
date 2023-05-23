from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('register/', views.create_new_user, name="register"),
]