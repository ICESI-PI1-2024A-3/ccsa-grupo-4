from django.urls import path
from . import views

urlpatterns = [
  
    path('', views.signup),
    path('event_checklist/', views.event_checklist)    
    path('singup/', views.home),
]