from django.urls import path, include

from core import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home-page"),

]