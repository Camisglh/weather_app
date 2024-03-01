from django.urls import path
from . import views

urlpatterns = {
    path("london/", views.get_weather, name="london"),
}
