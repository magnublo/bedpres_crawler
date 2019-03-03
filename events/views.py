from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from events import crawler
from events.models import CompanyEvent


class EventList(ListView):
    model = CompanyEvent
    def get_queryset(self):
        return CompanyEvent.objects.filter(user=self.request.user)

def run_crawl(request):
    crawler.run()
    return HttpResponse()