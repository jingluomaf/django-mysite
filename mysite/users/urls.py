from django.urls import path
from .views import register, profile
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView

app_name = 'user'
urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', PasswordResetView.as_view(
        template_name='users/password_reset.html'), name='password-reset'),
    path('password-reset/done', PasswordResetView.as_view(
        template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/<uidb64>/<token>', PasswordResetConfirmView.as_view(
        template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
