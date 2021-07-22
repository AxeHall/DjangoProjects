from django.shortcuts import render
from django.views.generic import View

class TeamListView(View):
    def get(self, request):
        return render(request, template_name="teams/team_list.html")

