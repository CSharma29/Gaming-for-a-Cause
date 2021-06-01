from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import View, ListView
from django.urls import reverse_lazy
from .forms import userRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import game_post

# Create your views here.

class home(LoginRequiredMixin, ListView):
    model = game_post
    raise_exception = True
    template_name = 'users/home.html'
    queryset = game_post.objects.all()


def register(request):
    
    if request.method == "POST":
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Account created for {username}!')
            return redirect('users:login')
    else:        
        form = userRegistrationForm()
    return render(request, "users/register.html", {"form": form})
