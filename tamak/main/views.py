from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import CustomUserCreationForm
from django.contrib import messages

class MainView(View):
    def get(self, request):
        return render(request, template_name="main/main.html")

class AboutView(View):
    def get(self, request):
        return render(request, template_name="main/about.html")

class FeedbacksView(View):
    def get(self, request):
        return render(request, template_name="main/feedbacks.html")

class RegistrationView (View):
    def get(self, request):
        register_form = CustomUserCreationForm()
        return render(request,template_name="main/registration.html", context={"register_form": register_form})

    def post(self, request):
        register_form = CustomUserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Your account has been created successfully")
            return redirect("login")
        errors = register_form.errors
        register_form = CustomUserCreationForm()

        return render(request,template_name="main/registration.html", context={"register_form": register_form, "errors": errors})