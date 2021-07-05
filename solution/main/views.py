from django.shortcuts import render
from django.views.generic import View


class MainView(View):
    def get(self, request):
        return render(request, template_name="main/wrapper.html")

class AboutView(View):
    def get(self, request):
        return render(request, template_name="main/about.html")

class HomeView(View):
    def get(self, request):
        return render(request, template_name="main/home.html", 
        context={
            "home_image_path": "images/learn-img.jpg",
            "home_title": "We are a Creative Digital Agency & Marketing Experts",
            "home_theme": "Pure Workflow. No Limits. Boundless configuration with best performance, more process control & resource savings",
            "home_description": "You don’t need to go to IT to create your own documents and spreadsheets. Why should processes be any different? Take charge of your processes, design your own forms and workflows, and bring automated efficiency to your team."
        })

class NewsView(View):
    def get(self, request):
        return render(request, template_name="main/news.html")

class ServicesView(View):
    def get(self, request):
        return render(request, template_name="main/services.html")

