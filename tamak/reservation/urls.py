from . import views
from django.urls import path


urlpatterns = [
    path("create/", views.ReservationCreateView.as_view(), name="reservation_create"),
    path("list/", views.ReservationListView.as_view(), name="reservation_list")
]
