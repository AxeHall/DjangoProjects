from django.urls import path
from .views import PrimaryMealsListView


urlpatterns = [
    path("meals/", PrimaryMealsListView.as_view(), name="meals")
]