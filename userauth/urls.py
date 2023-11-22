from django.urls import path
from . import views
from userauth import views
from .views import subscribe
from .views import login_view

app_name = "userauth"

urlpatterns = [
    path("sign-up/", views.register_view, name="sign-up"),
    path('subscribe/', subscribe, name='subscribe'),
    path('profile/', views.login_view, name='profile')
]