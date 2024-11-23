from django.urls import path
from .views import SignUpView, login_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path(r'signup/', SignUpView.as_view(), name='signup'),
    path(r'login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path(r'logout/', LogoutView.as_view(), name='logout'),
    path(r'profile/', )
]