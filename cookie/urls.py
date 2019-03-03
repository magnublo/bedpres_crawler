from django.urls import path

from cookie import views

urlpatterns = [
    path('new', views.CookieCreate.as_view(), name='cookie_new'),
]