from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import loginform,registrationform,userprofileform
from django.contrib.auth.decorators import login_required
from .models import userinfo, userprofile
from django.contrib.auth.models import User
from django.urls import reverse_lazy

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

def register(request):
    if request.method == 'POST':
        user_form=registrationform(request.POST)
        userprofile_form=userprofileform(request.POST)
        if user_form.is_valid()*userprofile_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile=userprofile_form.save(commit=False)
            new_profile.user=new_user
            new_profile.save()
            userinfo.objects.create(user=new_user)
            return HttpResponse("成功")
        else:
            return HttpResponse('注册失败')
    if request.method == 'GET':
        user_form=registrationform()
        userprofile_form=userprofileform()
        return render(request,'account/register.html',{'form':user_form,'profile':userprofile_form})
        
@login_required(login_url=reverse_lazy('account:user_login'))
def myself(request):
    user = User.objects.get(username=request.user.username)
    userprofile1 = userprofile.objects.get(user=user)
    userinfo1 = userinfo.objects.get(user=user)
    return render(request, "account/myself.html", {'user':user, 'userinfo':userinfo1,'userprofile':userprofile1})