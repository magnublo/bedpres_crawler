from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from accounts.models import User
from events import crawler
from events.models import CompanyEvent


class EventList(ListView):
    model = CompanyEvent
    def get_queryset(self):
        return CompanyEvent.objects.filter(user=self.request.user)

def run_crawl(request):
    crawler.run()
    return HttpResponse()

def toggle_crawl(request):
    user = User.objects.get(pk=request.user.pk)
    if user.crawl_is_toggled:
        user.crawl_is_toggled = False
    else:
        user.crawl_is_toggled = True
    user.save()
    return HttpResponseRedirect('/')