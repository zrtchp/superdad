from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import loginform

def user_login(request):
    if request.method == "POST":
        login_form=loginform(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user=authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                return HttpResponse('验证成功，欢迎登录。')
            else:
                return HttpResponse('用户名或密码错误')
        else:
            return HttpResponse("操作不合法")
    if request.method =="GET":
        login_form=loginform()
        return render(request, 'account/login.html',{'form':login_form})
