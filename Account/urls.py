from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import Register
urlpatterns =[
    path("login/", obtain_auth_token, name="login"),
    path("register/", Register.as_view(), name="register"),
]