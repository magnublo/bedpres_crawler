from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth import get_user_model
User = get_user_model()
from keywords.models import Keyword


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
