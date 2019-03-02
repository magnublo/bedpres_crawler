from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView
from cookie.models import Cookie
from django.contrib.auth import get_user_model
User = get_user_model()

class CookieList(ListView):
    model = Cookie
    def get_queryset(self):
        return Cookie.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class CookieCreate(CreateView):
    model = Cookie
    fields = ['value']
    success_url = reverse_lazy('cookie_list')

    def form_valid(self, form_class):
        form_class.instance.user = self.request.user
        return super().form_valid(form_class)


    def post(self, request, *args, **kwargs):
        # check for user logged in
        ...
        # check for user permission:
        # Take pk from kwargs
        pk = kwargs.get('pk')  # example
        # Take user from request
        user = User(request.user)
        # check permission
        cookies = Cookie.objects.filter(user=self.request.user)
        if len(cookies) is not 0:
            cookies.delete()
        return super(CookieCreate, self).post(request, *args, **kwargs)
