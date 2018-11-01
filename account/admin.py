from django.contrib import admin
from .models import userprofile, userinfo

class userprofileadmin(admin.ModelAdmin):
    list_display=('user','birth','phone')
    list_filter=("phone",)

class userinfoadmin(admin.ModelAdmin):
    list_display=("user",'school','company','profession','address','aboutme')
    list_filter=("user",)
    
admin.site.register(userprofile,userprofileadmin)
admin.site.register(userinfo,userinfoadmin)