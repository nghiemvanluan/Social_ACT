from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from allauth.account.views import PasswordChangeView, PasswordSetView

access_token = None
login_url = 'http://45.119.82.5:8088/social/api/login'
get_tags_url = 'http://45.119.82.5:8088/social/api/get_tags'


class MyPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy("dashboards:dashboard")


class MyPasswordSetView(PasswordSetView):
    success_url = reverse_lazy("dashboards:dashboard")


def account_login(request):
    login = request.POST.get('login')
    password = request.POST.get('password')
    body = {
        'username': login,
        'password': password
    }
    loginCMS = requests.post(login_url, data=body)
    login_json = loginCMS.json()
    if login_json["isSuccessful"] == True:
        access_token = login_json["access_token"]
        request.session['access_token'] = access_token
        request.session['message'] = 'Đăng nhập thành công!'
        tag = requests.get(get_tags_url).json()
        return render(request, 'dashboards/index.html')
    else:
        return redirect('/account/login/')


def dashboards(request):
    tag = requests.get(get_tags_url).json()
    print("Ssssssssssssssssss")
    print(tag)
    return render(request, 'dashboards/index.html',  {'tag': tag})
