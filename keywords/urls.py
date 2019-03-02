from django.urls import path

from . import views

urlpatterns = [
    path('', views.KeywordList.as_view(), name='keyword_list'),
    path('new', views.KeywordCreate.as_view(), name='keyword_new'),
    path('delete/<int:pk>', views.KeywordDelete.as_view(), name='keyword_delete'),
]