from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from . import forms

from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = forms.LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            name = form.cleaned_data.get("name")
            nickname = form.cleaned_data.get("nickname")
            password = form.cleaned_data.get("password")
            user = auth.authenticate(
                request=request,
                email=email,
                name=name,
                nickname=nickname,
                password=password,
            )
            if user is not None:
                auth.login(request, user)
                return redirect("core")
        return redirect("users:login")

    else:
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})


@login_required
def logout_view(request):
    auth.logout(request)
    return redirect("core")


def signup_view(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            auth.login(request, user)
            return redirect("core")
        return redirect("users:signup")

    else:
        form = forms.SignUpForm()
        return render(request, "users/signup.html", {"form": form})
