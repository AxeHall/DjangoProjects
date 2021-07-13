from django.urls import path
from .views import MainView, AboutView, NewsView, ServicesView
from .forms import CustomLoginForm
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", MainView.as_view(), name="main_view"),
    path("about/", AboutView.as_view(), name="main_about"),
    path("news/", NewsView.as_view(), name="main_news"),
    path("services/", ServicesView.as_view(), name="main_services"),
    path("login/", LoginView.as_view(template_name="main/home.html", authentication_form=CustomLoginForm), name="login"),
    path("logout/", LogoutView.as_view(template_name="main/logout.html"), name="logout")
]

