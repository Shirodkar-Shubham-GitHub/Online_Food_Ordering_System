from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_attempt, name="register_attempt"),
    path('accounts/login/', views.login_attempt, name="login_attempt"),
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('token', views.token_send, name="token_send"),
    path('verify/<auth_token>', views.verify , name="verify"),
    path('error', views.error_page, name="error"),
    path('forgot/', views.forgot, name='forgot'),
    path('verify_email/', views.verify_email, name='verify_email'),
    path('logout/', views.logout_request, name='logout'),
]
