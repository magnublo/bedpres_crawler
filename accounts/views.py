from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
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
