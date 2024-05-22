from django.urls import path
from rrp import views

urlpatterns = [
    path("", views.index, name="index"),
]