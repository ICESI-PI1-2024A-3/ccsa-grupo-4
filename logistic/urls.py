from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', views.admin, name = 'admin'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('event_checklist/', views.event_checklist)
]