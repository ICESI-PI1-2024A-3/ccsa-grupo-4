from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView

urlpatterns = [

    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('event_checklist/', views.event_checklist),
    path('password_reset', PasswordResetView.as_view(template_name='password_reset_form.html', email_template_name='password_reset.html'), name="password_reset"),
    path('password_reset_done', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/done', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]