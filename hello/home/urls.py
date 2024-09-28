from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("index", views.index, name='home'),
    path("about", views.about, name='about'),
    path("login", views.Login, name='login'),
    path("signup", views.register, name='signup'),
    path("history", views.history, name='history'),
    path("userprofile", views.userprofile, name='userprofile'),
    path('submit/', views.submit_text, name='submit_text'),
    path('history/delete/<int:id>/', views.delete_history, name='delete_history'),
]