from django.urls import path

from . import views

urlpatterns = [
    path('', views.CookieList.as_view(), name='cookie_list'),
    path('new', views.CookieCreate.as_view(), name='cookie_new'),
]