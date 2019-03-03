from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('events.urls')),
    path('', include('django.contrib.auth.urls')),
    path('keywords/', include('keywords.urls')),
    path('cookie/', include('cookie.urls')),
]
