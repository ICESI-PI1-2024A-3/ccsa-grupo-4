from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('event_checklist/', views.event_checklist)
]