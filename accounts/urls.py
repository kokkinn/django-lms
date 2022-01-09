from django.urls import path

from accounts.views import AccountRegistrationView, AccountLoginView, AccountLogoutView

app_name = "accounts"

urlpatterns = [
    path('registration/', AccountRegistrationView.as_view(), name='registration'),
    path('login/', AccountLoginView.as_view(), name="login"),
    path('logout/', AccountLogoutView.as_view(), name="logout"),
]
