from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', views.admin, name = 'admin'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('event/checklist/', views.event_checklist),
    path('create/event/', views.create_event, name= 'create_event'),
    path('create/task/', views.create_task, name= 'create_task'),
    path('edit/event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('edit/event/<int:event_id>/complete', views.complete_event, name='event_complete'),
    path('edit/event/<int:event_id>/delete', views.delete_event, name='event_delete'),
]