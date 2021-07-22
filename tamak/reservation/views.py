from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.views.generic import View, CreateView, ListView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ReservationCreateForm
from .models import Reservation


class ReservationCreateView(LoginRequiredMixin, FormView):
    template_name = 'reservation/reservations_create.html'
    form_class = ReservationCreateForm

    def get_success_url(self) -> str:
        return reverse("reservation_list")

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.client = self.request.user
        form.save()
        return super(ReservationCreateView, self).form_valid(form)

class ReservationListView(LoginRequiredMixin, ListView):
    template_name="reservation/reservations_list.html"
    model = Reservation
