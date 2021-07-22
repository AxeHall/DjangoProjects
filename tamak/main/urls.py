from django.urls import path
from django.views.generic.edit import DeleteView
from .views import MainView, FeedbackDeleteView, FeedbackUpdateView, AboutView, FeedbackListView, FeedbackCreateView, FeedbackDetailView


urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("about/", AboutView.as_view(), name="about"),
    path("feedback/create/", FeedbackCreateView.as_view(), name="feedback_create"),
    path("feedback/list/", FeedbackListView.as_view(), name="feedback_list"),
    path("feedback/details/<int:pk>", FeedbackDetailView.as_view(), name="feedback_details"),
    path("feedback/update/<int:pk>", FeedbackUpdateView.as_view(), name="feedback_update"),
    path("feedback/delete/<int:pk>", FeedbackDeleteView.as_view(), name="feedback_delete")
]
