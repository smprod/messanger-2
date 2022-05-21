from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginView(LoginView):
    template_name = 'registration/login.html'

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

class ProfileView(DetailView):
    model = User
    context_object_name = 'profile'
    template_name = 'registration/show_profile.html'
