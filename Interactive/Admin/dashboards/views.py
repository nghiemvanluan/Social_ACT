import requests
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from velzon.views import access_token


get_tags_url = 'http://45.119.82.5:8088/social/api/get_tags'
report_detail_url = "http://45.119.82.5:8088/social/api/report_detail"
comment_analysis_url = "http://45.119.82.5:8088/social/api/comment_analysis"


# Create your views here.


class DashboardView(LoginRequiredMixin, TemplateView):
    pass


def dashboards(request):
    access_token = request.session.get('access_token')
    headers = {'access_token': access_token}

    tag = requests.get(get_tags_url).json()

    if request.method == 'POST':
        print(request.POST.get('tag_id_check'))
        dataDefault = {
            'tag_id': request.POST.get('tag_id_check')
        }
    else:
        dataDefault = {
            'tag_id': 1
        }
    report_detail = requests.post(
        report_detail_url, headers=headers, data=dataDefault).json()
    comment_analysis = requests.post(
        comment_analysis_url, headers=headers, data=dataDefault).json()

    return render(request, 'dashboards/index.html',  {'tag': tag,
                                                      "report_detail": report_detail,
                                                      'comment_analysis': comment_analysis, })


# ---------------------------------------------
