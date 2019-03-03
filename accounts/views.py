from django.contrib.auth.forms import UserCreationForm
from django import forms
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
    cookie = forms.TextInput()

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
        return Cookie.objects.filter(user=self.request.user)

    context_object_name = "home"
    template_name = "home.html"
    #queryset = get_queryset(self)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['cookies'] = Cookie.objects.filter(user=self.request.user)
        context['keywords'] = Keyword.objects.filter(user=self.request.user)
        context['events'] = CompanyEvent.objects.filter(user=self.request.user)
        context['crawls'] = User.objects.filter(pk=self.request.user.pk)[0].last_crawl
        # And so on for more models
        return context
