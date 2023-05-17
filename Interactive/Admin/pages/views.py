from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import requests
# Create your views here.


delete_customer_url = 'http://45.119.82.5:8088/social/api/delete_customer'
user_url = "http://45.119.82.5:8088/social/api/get_user_info"
logout_url = "http://45.119.82.5:8088/social/api/logout"
tags_url = "http://45.119.82.5:8088/social/api/get_tags"
register_url = "http://45.119.82.5:8088/social/api/register"


class PagesView(TemplateView):
    pass


# Authenticatin
authentication_signin_basic = PagesView.as_view(
    template_name="pages/authentication/auth-signin-basic.html")
authentication_signin_cover = PagesView.as_view(
    template_name="pages/authentication/auth-signin-cover.html")
authentication_signup_basic = PagesView.as_view(
    template_name="pages/authentication/auth-signup-basic.html")
authentication_signup_cover = PagesView.as_view(
    template_name="pages/authentication/auth-signup-cover.html")
authentication_pass_reset_basic = PagesView.as_view(
    template_name="pages/authentication/auth-pass-reset-basic.html")
authentication_pass_reset_cover = PagesView.as_view(
    template_name="pages/authentication/auth-pass-reset-cover.html")
authentication_lockscreen_basic = PagesView.as_view(
    template_name="pages/authentication/auth-lockscreen-basic.html")
authentication_lockscreen_cover = PagesView.as_view(
    template_name="pages/authentication/auth-lockscreen-cover.html")
authentication_logout_basic = PagesView.as_view(
    template_name="pages/authentication/auth-logout-basic.html")
authentication_logout_cover = PagesView.as_view(
    template_name="pages/authentication/auth-logout-cover.html")
authentication_success_msg_basic = PagesView.as_view(
    template_name="pages/authentication/auth-success-msg-basic.html")
authentication_success_msg_cover = PagesView.as_view(
    template_name="pages/authentication/auth-success-msg-cover.html")
authentication_twostep_basic = PagesView.as_view(
    template_name="pages/authentication/auth-twostep-basic.html")
authentication_twostep_cover = PagesView.as_view(
    template_name="pages/authentication/auth-twostep-cover.html")
authentication_404_basic = PagesView.as_view(
    template_name="pages/authentication/auth-404-basic.html")
authentication_404_cover = PagesView.as_view(
    template_name="pages/authentication/auth-404-cover.html")
authentication_404_alt = PagesView.as_view(
    template_name="pages/authentication/auth-404-alt.html")
authentication_500 = PagesView.as_view(
    template_name="pages/authentication/auth-500.html")
# Pages
pages_starter = PagesView.as_view(template_name="pages/pages-starter.html")
pages_profile = PagesView.as_view(template_name="pages/pages-profile.html")
pages_profile_settings = PagesView.as_view(
    template_name="pages/pages-profile-settings.html")
pages_team = PagesView.as_view(template_name="pages/pages-team.html")
pages_timeline = PagesView.as_view(template_name="pages/pages-timeline.html")
pages_faqs = PagesView.as_view(template_name="pages/pages-faqs.html")
pages_pricing = PagesView.as_view(template_name="pages/pages-pricing.html")
pages_gallery = PagesView.as_view(template_name="pages/pages-gallery.html")
pages_maintenance = PagesView.as_view(
    template_name="pages/pages-maintenance.html")
pages_coming_soon = PagesView.as_view(
    template_name="pages/pages-coming-soon.html")
pages_sitemap = PagesView.as_view(template_name="pages/pages-sitemap.html")
pages_search_results = PagesView.as_view(
    template_name="pages/pages-search-results.html")

pages_landing = PagesView.as_view(template_name="pages/pages-landing.html")


def user(request):
    access_token = request.session.get('access_token')
    headers = {'access_token': access_token}
    user = requests.post(user_url, headers=headers).json()
    return render(request, 'pages/pages-user.html', {
        'user': user})


def logout(request):
    access_token = request.session.get('access_token')
    headers = {'access_token': access_token}
    requests.post(
        logout_url, headers=headers).json()
    return redirect('/')


def Signup(request):
    tags = requests.get(tags_url).json()
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('name')
        password = request.POST.get('password')
        tag_id = request.POST.get('tags')
        data = {
            'email': email,
            'username': username,
            'password': password,
            'tag_id': tag_id
        }
        requests.post(
            register_url, data=data).json()
        return redirect('/')
    return render(request, 'account/signup.html', {'tags': tags})
