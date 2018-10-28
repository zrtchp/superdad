from django.contrib import admin
from .models import userprofile

class userprofileadmin(admin.ModelAdmin):
    list_display=('user','birth','phone')
    list_filter=("phone",)

admin.site.register(userprofile,userprofileadmin)