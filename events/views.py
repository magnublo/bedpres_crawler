from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from events.models import CompanyEvent


class CookieList(ListView):
    model = CompanyEvent
    def get_queryset(self):
        return CompanyEvent.objects.filter(user=self.request.user)