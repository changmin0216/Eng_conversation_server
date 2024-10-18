from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, logout_then_login, LogoutView
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from accounts.forms import SignupForm


login = LoginView.as_view(template_name='accounts/login_form.html')

def logout(request):
    messages.success(request, '로그아웃되었습니다.')
    return logout_then_login(request)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            messages.success(request, '회원가입을 환영합니다. 다시 로그인 해주세요')
            next_url = request.GET.get('/text', '/')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form':form
    })