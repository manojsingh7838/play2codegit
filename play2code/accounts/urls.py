from django.urls import path
from .views import (
    signup_view,
    otp_verification_view,
    login_view,
    signup_view,
    logout_view,
    home
)

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("otp-auth/", otp_verification_view, name="otp_auth"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("", home, name="home"),
]
