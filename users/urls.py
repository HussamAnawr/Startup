from django.urls import path, include, re_path
from allauth.account.views import confirm_email
####
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView
from dj_rest_auth.views import LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    # path('account/', include('allauth.urls')),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    path("signup/", include("dj_rest_auth.registration.urls")),
    path("verify-email/", VerifyEmailView.as_view(), name="rest_verify_email"),
]