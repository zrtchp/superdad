from django import forms
from django.contrib.auth.models import User
from .models import userprofile, userinfo

class loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    
class registrationform(forms.ModelForm):
    password=forms.CharField(label="Password", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=('username','email')

    def clean_password2(self):
        cd=self.cleaned_data
        
        if cd['password']!=cd['password2']:
            raise forms.ValidationError("passwords do not match.")
        return cd['password2']
    
class userprofileform(forms.ModelForm):
    class Meta:
        model=userprofile
        fields=("phone","birth")

class userinfoform(forms.ModelForm):
    class Meta:
        model = userinfo
        fields = ("school","company",'profession','address','aboutme')

class userform(forms.Modelform):
    class Meta:
        model = user
        fields = ("email",)