from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView, ListView, FormView
from .models import CustomUser
from .forms import LoginForm
from .forms import CustomUserForm
from django.conf import settings
class ThankYouView(TemplateView):
    template_name = "common/thank_you.html"

class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserForm  # 위에서 정의한 폼 클래스 사용
    success_url = reverse_lazy("common:login")

class UserListView(ListView):
    #model_list.html을 자동으로 찾음
    model = CustomUser
def LogoutView(request):
    # 홈페이지 뷰 로직
    now_user = settings.GLOBAL_LOGIN_USER
    user = CustomUser.objects.get(username=now_user)
    user.is_login = False
    user.save()
    settings.IS_NOW_LOGIN = False
    return redirect(reverse('home'))

class LoginView(FormView):
    template_name = 'common/login.html'
    form_class = LoginForm
    success_url = reverse_lazy("home")

    # LoginView.as_view()가 실행될 때
    def form_valid(self, form):
        self.request.session['user'] = form.username
        settings.GLOBAL_LOGIN_USER = form.username
        settings.IS_NOW_LOGIN = True
        return super().form_valid(form)


