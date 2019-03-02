from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView

from keywords.models import Keyword, Cookie


class KeywordList(ListView):
    model = Keyword
    def get_queryset(self):
        return Keyword.objects.filter(user=self.request.user)

class KeywordCreate(CreateView):
    model = Keyword
    fields = ['value']
    success_url = reverse_lazy('keyword_list')

class KeywordDelete(DeleteView):
    model = Keyword
    success_url = reverse_lazy('keyword_list')

    def dispatch(self, request, *args, **kwargs):
        # check for user logged in
        ...
        # check for user permission:
        # Take pk from kwargs
        pk = kwargs.get('pk')  # example
        # Take user from request
        user = request.user
        # check permission
        try:
            Keyword.objects.get(pk=pk, user=user)
            return super(KeywordDelete, self).dispatch(request, *args, **kwargs)
        except Keyword.DoesNotExist as e:
            return HttpResponseForbidden()

class CookieList(ListView):
    model = Cookie
    def get_queryset(self):
        return Cookie.objects.filter(user=self.request.user)

class CookieCreate(CreateView):
    model = Cookie
    fields = ['value']
    success_url = reverse_lazy('cookie_list')


    def post(self, request, *args, **kwargs):
        # check for user logged in
        ...
        # check for user permission:
        # Take pk from kwargs
        pk = kwargs.get('pk')  # example
        # Take user from request
        user = request.user
        # check permission
        cookies = Cookie.objects.filter(user=self.request.user)
        if len(cookies) is not 0:
            cookies.delete()
        return super(CookieCreate, self).post(request, *args, **kwargs)
