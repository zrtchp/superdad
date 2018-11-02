from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login
from .forms import loginform,registrationform,userprofileform,userform,userinfoform
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
            return render(request,'account/register-results.html',{'results':'注册成功',})
        else:
            return render(request,'account/register-results.html',{'results':'注册失败',})
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

@login_required(login_url=reverse_lazy('account:user_login'))
def myself_edit(request):
    user = User.objects.get(username=request.user.username)
    userprofile1 = userprofile.objects.get(user=request.user)
    userinfo1 = userinfo.objects.get(user=request.user)

    if request.method == "POST":
        user_form = userform(request.POST)
        userprofile_form = userprofileform(request.POST)
        userinfo_form = userinfoform(request.POST)
        if user_form.is_valid() * userprofile_form.is_valid() * userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            print(user_cd["email"])
            user.email = user_cd["email"]
            userprofile1.birth = userprofile_cd['birth']
            userprofile1.phone = userprofile_cd['phone']
            userinfo1.school = userinfo_cd['school']
            userinfo1.company = userinfo_cd['company']
            userinfo1.profession = userinfo_cd['profession']
            userinfo1.address = userinfo_cd['address']
            userinfo1.aboutme = userinfo_cd['aboutme']
            user.save()
            userprofile1.save()
            userinfo1.save()
        return HttpResponseRedirect(reverse_lazy("account:my_information"))
    else:
        user_form = userform(instance=request.user)
        userprofile_form = userprofileform(initial={'birth':userprofile1.birth,"phone":userprofile1.phone})
        userinfo_form = userinfoform(initial={'school':userinfo1.school,'company':userinfo1.company,'profession':userinfo1.profession,'address':userinfo1.address,'aboutme':userinfo1.aboutme})
        return render(request,'account/myself_edit.html',{'user_form':user_form,'userprofile_form':userprofile_form,'userinfo_form':userinfo_form})

@login_required(login_url=reverse_lazy('account:login'))
def my_image(request):
    if request.method == "POST":
        img = request.POST['img']
        userinfo1 = userinfo.objects.get(user=request.user.id)
        userinfo1.photo = img
        userinfo1.save()
        return HttpResponse("1")
    else:
        return render(request,'account/imagecrop.html',)