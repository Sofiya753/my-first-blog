from django.urls import  path, include
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.index, name='homePage',),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

]
