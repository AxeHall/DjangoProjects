from django.urls import path
from .views import MainView, AboutView, HomeView, NewsView, ServicesView

urlpatterns = [
    path("wrapper", MainView.as_view(), name="main_view"),
    path("home/", HomeView.as_view(), name="main_home"),
    path("about/", AboutView.as_view(), name="main_about"),
    path("news/", NewsView.as_view(), name="main_news"),
    path("services/", ServicesView.as_view(), name="main_services"),
]
