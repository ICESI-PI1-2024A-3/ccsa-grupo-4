from django.contrib import admin
from django.urls import path
from logistic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('result/', views.user_detail, name='user_detail'),
    path('', views.search_users, name='search_users'),
]
