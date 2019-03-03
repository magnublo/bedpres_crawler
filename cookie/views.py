from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from cookie.models import Cookie

User = get_user_model()

@method_decorator(login_required, name='dispatch')
class CookieCreate(CreateView):
    model = Cookie
    fields = ['value']
    success_url = reverse_lazy('home')

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
