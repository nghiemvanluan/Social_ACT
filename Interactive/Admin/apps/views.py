import requests
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from velzon.views import access_token
from django.contrib import messages

track_list_url = 'http://45.119.82.5:8088/social/api/track_list'
status_c_url = 'http://45.119.82.5:8088/social/api/switch_track_status'
delete_source_url = 'http://45.119.82.5:8088/social/api/delete_tracking'
get_sources_url = 'http://45.119.82.5:8088/social/api/get_sources'
get_tags_url = 'http://45.119.82.5:8088/social/api/get_tags'
list_customer_url = 'http://45.119.82.5:8088/social/api/list_suggest'
create_tracking_url = 'http://45.119.82.5:8088/social/api/create_tracking'
search_customers_url = 'http://45.119.82.5:8088/social/api/search_customers'
save_customer_url = 'http://45.119.82.5:8088/social/api/save_customer'
get_customers_url = 'http://45.119.82.5:8088/social/api/get_customers'
detail_customer_url = 'http://45.119.82.5:8088/social/api/detail_customer'
delete_customer_url = 'http://45.119.82.5:8088/social/api/delete_customer'

# Create your views here.


class AppsView(LoginRequiredMixin, TemplateView):
    pass


# Calendar
apps_calendar_view = AppsView.as_view(template_name="apps/apps-calendar.html")
# Chat
apps_chat_view = AppsView.as_view(template_name="apps/apps-chat.html")
# Mail Box
apps_mailbox_view = AppsView.as_view(template_name="apps/apps-mailbox.html")

# Ecommerce
apps_ecommerce_products_view = AppsView.as_view(
    template_name="apps/ecommerce/apps-ecommerce-products.html")
apps_ecommerce_product_details_view = AppsView.as_view(
    template_name="apps/ecommerce/apps-ecommerce-product-details.html")
apps_ecommerce_add_product_view = AppsView.as_view(
    template_name="apps/ecommerce/apps-ecommerce-add-product.html")
apps_ecommerce_orders_view = AppsView.as_view(
    template_name="apps/ecommerce/apps-ecommerce-orders.html")
apps_ecommerce_order_details_view = AppsView.as_view(
    template_name="apps/ecommerce/apps-ecommerce-order-details.html")
apps_ecommerce_customers_view = AppsView.as_view(
    template_name="apps/ecommerce/apps-ecommerce-customers.html")
apps_ecommerce_cart_view = AppsView.as_view(
    template_name="apps/ecommerce/apps-ecommerce-cart.html")
apps_ecommerce_checkout_view = AppsView.as_view(
    template_name="apps/ecommerce/apps-ecommerce-checkout.html")
apps_ecommerce_sellers_view = AppsView.as_view(
    template_name="apps/ecommerce/apps-ecommerce-sellers.html")
apps_ecommerce_seller_details_view = AppsView.as_view(
    template_name="apps/ecommerce/apps-ecommerce-seller-details.html")

# Projects
apps_projects_list_view = AppsView.as_view(
    template_name="apps/projects/apps-projects-list.html")
apps_projects_overview_view = AppsView.as_view(
    template_name="apps/projects/apps-projects-overview.html")
apps_projects_create_view = AppsView.as_view(
    template_name="apps/projects/apps-projects-create.html")

# Tasks
apps_tasks_kanban_view = AppsView.as_view(
    template_name="apps/tasks/apps-tasks-kanban.html")
apps_tasks_list_view = AppsView.as_view(
    template_name="apps/tasks/apps-tasks-list-view.html")
apps_tasks_details_view = AppsView.as_view(
    template_name="apps/tasks/apps-tasks-details.html")

# CRM
apps_crm_contacts_view = AppsView.as_view(
    template_name="apps/crm/apps-crm-contacts.html")
apps_crm_companies_view = AppsView.as_view(
    template_name="apps/crm/apps-crm-companies.html")
apps_crm_deals_view = AppsView.as_view(
    template_name="apps/crm/apps-crm-deals.html")
apps_crm_leads_view = AppsView.as_view(
    template_name="apps/crm/apps-crm-leads.html")

# Crypto
apps_crypto_transactions_view = AppsView.as_view(
    template_name="apps/crypto/apps-crypto-transactions.html")
apps_crypto_buy_sell_view = AppsView.as_view(
    template_name="apps/crypto/apps-crypto-buy-sell.html")
apps_crypto_orders_view = AppsView.as_view(
    template_name="apps/crypto/apps-crypto-orders.html")
apps_crypto_wallet_view = AppsView.as_view(
    template_name="apps/crypto/apps-crypto-wallet.html")
apps_crypto_ico_view = AppsView.as_view(
    template_name="apps/crypto/apps-crypto-ico.html")
apps_crypto_kyc_view = AppsView.as_view(
    template_name="apps/crypto/apps-crypto-kyc.html")

# Invoices
apps_invoices_list_view = AppsView.as_view(
    template_name="apps/invoices/apps-invoices-list.html")
apps_invoices_details_view = AppsView.as_view(
    template_name="apps/invoices/apps-invoices-details.html")
apps_invoices_create_view = AppsView.as_view(
    template_name="apps/invoices/apps-invoices-create.html")

# Support Tickets
apps_tickets_list_view = AppsView.as_view(
    template_name="apps/support-tickets/apps-tickets-list.html")
apps_tickets_details_view = AppsView.as_view(
    template_name="apps/support-tickets/apps-tickets-details.html")


def source(request):
    access_token = request.session.get('access_token')
    headers = {
        'access_token': access_token
    }
    data_list_suggest = {
        'source_id': 1,
        'tag_id': 1,
    }
    response = requests.get(get_sources_url).json()
    tag = requests.get(get_tags_url).json()
    list_suggest = requests.post(
        list_customer_url, data=data_list_suggest, headers=headers).json()
    track_list = requests.post(track_list_url, headers=headers).json()

    check = False
    if request.method == 'POST':
        source_id = request.POST.get('source_id')
        keyword = request.POST.get('keyword')
        tag_id = request.POST.get('tag_id')
        is_custom = False
        is_status = False
        if request.POST.get('status') == 'on':
            is_status = True
        data = {
            'source_id': source_id,
            'keyword': keyword.split(":")[0],
            'name': keyword.split(":")[1],
            'tag_id': tag_id,
            'is_custom': is_custom,
            'status': is_status
        }

        for item in track_list:
            if item['keyword'] == keyword.split(":")[0]:
                check = True

        if check == False:
            requests.post(
                create_tracking_url, data=data, headers=headers)
        return redirect('/source-clients/')

    return render(request, 'apps/ecommerce/nguon.html', {
        'track_list': track_list,
        'response': response,
        'tag': tag,
        'list_suggest': list_suggest,
    })


def sourceJs(request):

    access_token = request.session.get('access_token')
    headers = {
        'access_token': access_token
    }
    if request.method == 'GET':
        dataLS = {
            'source_id': request.GET.get('source_id'),
            'tag_id': request.GET.get('tag_id')
        }
        list_suggest = requests.post(
            list_customer_url, data=dataLS, headers=headers).json()
        return JsonResponse({'list_suggest': list_suggest})


def status_c(request, source_id, status):
    print(source_id)
    print(status)
    access_token = request.session.get('access_token')
    headers = {'access_token': access_token}
    if status == 'False':
        data = {'track_id': source_id,
                'status': True}
    else:
        data = {'track_id': source_id,
                'status': False}
    requests.post(
        status_c_url, headers=headers, data=data).json()
    return redirect('/source-clients/')


def delete_source(request):
    access_token = request.session.get('access_token')
    headers = {
        'access_token': access_token
    }
    if request.method == 'GET':
        dataLS = {
            'track_id': int(request.GET.get('source_id')),
        }
    requests.post(
        delete_source_url, headers=headers, data=dataLS)
    return redirect('/source-clients/')


def clients(request):
    access_token = request.session.get('access_token')
    headers = {
        'access_token': access_token
    }
    get_tags = requests.get(get_tags_url).json()
    get_customers = requests.post(get_customers_url, headers=headers).json()
    search_customers = None
    check = False
    if request.method == 'POST':
        source_id_check = request.POST.get('sources_id_check')
        mess_input = request.POST.get('mess_input')
        tag_id_check = request.POST.get('tag_id_check')
        data = {
            'keyword': mess_input,
            'tag_id': tag_id_check,
        }
        search_customers = requests.post(
            search_customers_url, data=data, headers=headers).json()

        name = request.POST.get('name_kh')
        if name != None:
            name = request.POST.get('name_kh')
            customer_name = request.POST.get('name')
            group_id = request.POST.get('group_id')
            group_name = request.POST.get('group_name')
            profile_url = request.POST.get('profile_url')
            source_id = source_id_check
            tag_id = tag_id_check
            keyword = mess_input
            is_custom = False

            dataSave = {
                'name': name,
                'customer_name': customer_name,
                'group_id': group_id,
                'group_name': group_name,
                'profile_url': profile_url,
                'source_id': source_id,
                'tag_id': tag_id,
                'keyword': keyword,
                'is_custom': is_custom
            }
            for item in get_customers:
                if item['profile_url'] == profile_url:
                    check = True
            if check == False:
                requests.post(
                    save_customer_url, data=dataSave, headers=headers).json()
            else:
                messages.success(request, 'Lưu dữ liệu thành công!',
                                 extra_tags='success|autodismiss')
    return render(request, 'apps/ecommerce/khach-tiem-nang.html', {'tags': get_tags, 'search_customers': search_customers, })


def list_customer(request):
    access_token = request.session.get('access_token')
    headers = {
        'access_token': access_token
    }
    get_customers = requests.post(get_customers_url, headers=headers).json()
    return render(request, 'apps/crm/apps-crm-leads.html', {'get_customers': get_customers})


def detail_customer(request, customer_id):
    access_token = request.session.get('access_token')
    headers = {'access_token': access_token}
    data = {'customer_id': customer_id}
    detail_customer = requests.post(
        detail_customer_url, headers=headers, data=data).json()
    return render(request, 'apps/crm/apps-crm-companies.html', {'detail_c': detail_customer})


def delete_customer(request):
    access_token = request.session.get('access_token')
    headers = {
        'access_token': access_token
    }
    if request.method == 'GET':
        dataLS = {
            'customer_id': int(request.GET.get('customer_id')),
        }
    requests.post(
        delete_customer_url, headers=headers, data=dataLS)
    return redirect('/source-clients/list_customers/')

    # access_token = request.session.get('access_token')
    # headers = {'access_token': access_token}
    # data = {'customer_id': customer_id}
    # delete_customer = requests.post(
    #     delete_customer_url, headers=headers, data=data).json()
    # return redirect('/clients/list_customers/')


def typical_comment(request, search):
    print(search)

    return render(request, '/source-clients/list_customers/')


def post_all(request):
    return render(request, 'apps/projects/apps-projects-list.html')


def post_new(request):
    return render(request, 'apps/projects/apps-projects-create.html')


def campaign_new(request):
    return render(request, 'apps/projects/apps-projects-campaign.html')


def campaign_manage(request):
    return render(request, 'apps/projects/apps-projects-campaign-manage.html')
