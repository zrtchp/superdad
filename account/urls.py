from django.urls import path,reverse_lazy
from . import views

#from django.conf import settings
from django.contrib.auth import views as auth_views

app_name='account'
urlpatterns = [
    #path("login",views.user_login,name="user_login"),
    path('login',auth_views.LoginView.as_view(template_name='account/login.html'),name='user_login'),
    path('logout',auth_views.LogoutView.as_view(template_name='account/logout.html'),name="user_logout"),
    path('register',views.register,name="user_register"),
    path('password-change',auth_views.PasswordChangeView.as_view(success_url=reverse_lazy("account:password_change_done"),template_name="account/password_change.html"),name="password_change"),
    path('password-change-done',auth_views.PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"),name="password_change_done"),
    path('password-reset',auth_views.PasswordResetView.as_view(email_template_name = 'account/password_reset_email.html', subject_template_name = 'account/password_reset_subject.txt', success_url = reverse_lazy('account:password_reset_done'),template_name = 'account/password_reset_form.html'
   ),name="password_reset"),
    path('password-reset-done',auth_views.PasswordResetDoneView.as_view(template_name = 'account/password_reset_done.html'),name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(success_url = reverse_lazy('account:password_reset_complete'), template_name = 'account/password_reset_confirm.html'),name="password_reset_confirm"),
    path('password-reset-complete',auth_views.PasswordResetCompleteView.as_view(template_name = 'account/password_reset_complete.html'),name="password_reset_complete"),
]
