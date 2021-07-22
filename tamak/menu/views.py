from django.shortcuts import render
from django.views.generic import View, ListView


class PrimaryMealsListView(ListView):
    template_name="menu/primary_meals.html"

