from django.urls import path
from . import views
from django.views.generic import View

app_name = "mario"

urlpatterns = [
    path("", views.home, name= "home")
]