from django.urls import path
from . import views

#all the urls for our different page views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logout_request, name='logout')
]