from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class AppsView(LoginRequiredMixin,TemplateView):
    pass

# Calendar
apps_calendar_view = AppsView.as_view(template_name="apps/apps-calendar.html")
# Chat
apps_chat_view = AppsView.as_view(template_name="apps/apps-chat.html")
# Mail Box
apps_mailbox_view = AppsView.as_view(template_name="apps/apps-mailbox.html")

# Ecommerce
apps_ecommerce_products_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-products.html")
apps_ecommerce_product_details_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-product-details.html")
apps_ecommerce_add_product_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-add-product.html")
apps_ecommerce_orders_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-orders.html")
apps_ecommerce_order_details_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-order-details.html")
apps_ecommerce_customers_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-customers.html")
apps_ecommerce_cart_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-cart.html")
apps_ecommerce_checkout_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-checkout.html")
apps_ecommerce_sellers_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-sellers.html")
apps_ecommerce_seller_details_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-seller-details.html")

# Projects
apps_projects_list_view = AppsView.as_view(template_name="apps/projects/apps-projects-list.html")
apps_projects_overview_view = AppsView.as_view(template_name="apps/projects/apps-projects-overview.html")
apps_projects_create_view = AppsView.as_view(template_name="apps/projects/apps-projects-create.html")

# Tasks
apps_tasks_kanban_view = AppsView.as_view(template_name="apps/tasks/apps-tasks-kanban.html")
apps_tasks_list_view = AppsView.as_view(template_name="apps/tasks/apps-tasks-list-view.html")
apps_tasks_details_view = AppsView.as_view(template_name="apps/tasks/apps-tasks-details.html")

# CRM
apps_crm_contacts_view = AppsView.as_view(template_name="apps/crm/apps-crm-contacts.html")
apps_crm_companies_view = AppsView.as_view(template_name="apps/crm/apps-crm-companies.html")
apps_crm_deals_view = AppsView.as_view(template_name="apps/crm/apps-crm-deals.html")
apps_crm_leads_view = AppsView.as_view(template_name="apps/crm/apps-crm-leads.html")

# Crypto
apps_crypto_transactions_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-transactions.html")
apps_crypto_buy_sell_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-buy-sell.html")
apps_crypto_orders_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-orders.html")
apps_crypto_wallet_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-wallet.html")
apps_crypto_ico_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-ico.html")
apps_crypto_kyc_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-kyc.html")

# Invoices
apps_invoices_list_view = AppsView.as_view(template_name="apps/invoices/apps-invoices-list.html")
apps_invoices_details_view = AppsView.as_view(template_name="apps/invoices/apps-invoices-details.html")
apps_invoices_create_view = AppsView.as_view(template_name="apps/invoices/apps-invoices-create.html")

# Support Tickets
apps_tickets_list_view = AppsView.as_view(template_name="apps/support-tickets/apps-tickets-list.html")
apps_tickets_details_view = AppsView.as_view(template_name="apps/support-tickets/apps-tickets-details.html")