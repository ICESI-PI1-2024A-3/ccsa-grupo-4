from django.contrib import admin
from django.urls import path
from django.urls import include
from logistic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('logistic.urls'))

]
