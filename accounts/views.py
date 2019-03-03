import datetime

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from django.views.generic import ListView

from cookie.models import Cookie
from events.models import CompanyEvent
from keywords.models import Keyword

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    last_crawl = datetime.MINYEAR
    success_url = reverse_lazy('home')
    class Meta:
        model = get_user_model()
        fields = ['username','email']

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    class Meta:
        model = get_user_model()

class IndexView(ListView):
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Cookie.objects.filter(user=self.request.user)
        else:
            return None

    context_object_name = "home"
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            return context
        context['cookies'] = Cookie.objects.filter(user=self.request.user)
        context['keywords'] = Keyword.objects.filter(user=self.request.user)
        context['events'] = CompanyEvent.objects.filter(user=self.request.user)
        context['last_crawl'] = User.objects.get(pk=self.request.user.pk).last_crawl
        context['crawl_toggled'] = User.objects.get(pk=self.request.user.pk).crawl_is_toggled
        # And so on for more models
        return context
