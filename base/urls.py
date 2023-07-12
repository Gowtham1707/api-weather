from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("api_view", api_response, name="api_response")
]
