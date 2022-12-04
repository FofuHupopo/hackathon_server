from django.shortcuts import render
from django.views import View
from django.core.handlers.wsgi import WSGIRequest


class CampListView(View):
    def get(self, request: WSGIRequest):
        
        return render(
            request,
            "crm/index.html",
            {}
        )
