from django.urls import path
from .views import MainView, AboutView, FeedbacksView


urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("about/", AboutView.as_view(), name="about"),
    path("feedback/", FeedbacksView.as_view(), name="feedback"),
]
