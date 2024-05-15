from django.urls import path
from rrp import views

urlpatterns = [
    path("", views.home, name="home"),
]