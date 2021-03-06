from django.urls import path

from events import views

urlpatterns = [
    path('', views.EventList.as_view(), name='event_list'),
    path('run_crawl', views.run_crawl, name='run_crawl'),
    path('toggle_crawl', views.toggle_crawl, name='toggle_crawl'),
]