from django.urls import path, include

from core import views

urlpatterns = [
    path("", views.ContactUsView.as_view(), name="home-page"),
    path("blog", views.BlogPageView.as_view(), name="blog-page"),


]