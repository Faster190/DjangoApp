from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import RegisterForm
from .models import *

# Create your views here.
def home(requset):
    return redirect("main")

def registration(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        email = request.POST.get("email")
        age = request.POST.get("age")
        if password != repeat_password:
            context["error"] = "Пароли не совпадают"
        if int(age) < 18:
            context["error"] = "Вы должны быть старше 18"
        if User.objects.filter(nickname=username):
            context["error"] = "Пользователь уже существует"
        if not context:
            User.objects.create(nickname=username, email=email, password=password, age=age)
            return HttpResponse(f"Приветствуем, {username}!")
    return render(request, "RegLog/registration_page.html", context)

@login_required
def profile_view(request):
    return render(request, 'RegLog/profile.html')

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def logout_user(request):
    logout(request)
    return redirect("main")