from django.shortcuts import render,redirect,get_object_or_404
from .forms import CustomUserCreationForm,CustomUserChangeForm

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib.auth.forms import (
    AuthenticationForm,
)
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from .models import User
from django.contrib.auth.decorators import login_required


# 회원가입 (GET - 회원가입폼 보내기) // (POST - 사용자가 입력한 개인정보 디비저장)
@require_http_methods(['GET', 'POST'])
def signup(request):
    
    # 이미 로그인되어있는 사람은 접근 금지
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #회원가입과 동시에 로그인해주기
            auth_login(request,user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/form.html',context)


@require_http_methods(['GET','POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method =='POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/form.html', context)


@require_http_methods(['POST'])
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('articles:index')


#profile
def profile(request,username):
    person = get_object_or_404(get_user_model(),username=username)
    context = {
        'person' : person,
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def update(request):
    print('ho')
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)