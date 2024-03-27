from django.urls import path
from django.contrib import admin
from .views import task
from .views import event
from .views import user

urlpatterns = [
    path('admin/', user.admin, name='admin'),
    path('home/', user.home, name='home'),
    path('signup/', user.signup, name='signup'),
    path('logout/', user.signout, name='logout'),
    path('', user.signin, name='signin'),
    path('signin/', user.signin, name='signin'),
    path('event/checklist/<int:event_id>',
         event.event_checklist, name='event_checklist'),
    path('create/event/', event.create_event, name='create_event'),
    path('create/task/', task.create_task, name='create_task'),
    path('edit/event/<int:event_id>/', event.edit_event, name='edit_event'),
    path('edit/event/<int:event_id>/complete',
         event.complete_event, name='event_complete'),
    path('edit/event/<int:event_id>/delete',
         event.delete_event, name='event_delete'),
    path('home/search/', user.search_user, name='users_search')
]
