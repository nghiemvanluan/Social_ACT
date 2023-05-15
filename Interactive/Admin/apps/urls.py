from django.urls import path
from apps.views import (
    apps_calendar_view,
    apps_chat_view,
    apps_mailbox_view,
    apps_ecommerce_products_view,
    apps_ecommerce_product_details_view,
    apps_ecommerce_add_product_view,
    apps_ecommerce_orders_view,
    apps_ecommerce_order_details_view,
    apps_ecommerce_customers_view,
    apps_ecommerce_cart_view,
    apps_ecommerce_checkout_view,
    apps_ecommerce_sellers_view,
    apps_ecommerce_seller_details_view,
    apps_projects_list_view,
    apps_projects_overview_view,
    apps_projects_create_view,
    apps_tasks_kanban_view,
    apps_tasks_list_view,
    apps_tasks_details_view,
    apps_crm_contacts_view,
    apps_crm_companies_view,
    apps_crm_deals_view,
    apps_crm_leads_view,
    apps_crypto_transactions_view,
    apps_crypto_buy_sell_view,
    apps_crypto_orders_view,
    apps_crypto_wallet_view,
    apps_crypto_ico_view,
    apps_crypto_kyc_view,
    apps_invoices_list_view,
    apps_invoices_details_view,
    apps_invoices_create_view,
    apps_tickets_list_view,
    apps_tickets_details_view
)
from .views import source, status_c, delete_source, sourceJs, clients, list_customer, detail_customer, delete_customer, typical_comment
app_name = "apps"

urlpatterns = [
    # Calendar
    path("calendar", view=apps_calendar_view, name="calendar"),
    # Chat
    path("chat", view=apps_chat_view, name="chat"),
    path("mailbox", view=apps_mailbox_view, name="mailbox"),
    # Ecommerce
    path("ecommerce/products", view=apps_ecommerce_products_view,
         name="ecommerce.products"),
    path("ecommerce/product-details", view=apps_ecommerce_product_details_view,
         name="ecommerce.product_details"),
    path("ecommerce/add-product", view=apps_ecommerce_add_product_view,
         name="ecommerce.add_product"),
    path("ecommerce/orders", view=apps_ecommerce_orders_view,
         name="ecommerce.orders"),
    path("ecommerce/order-details", view=apps_ecommerce_order_details_view,
         name="ecommerce.order_details"),

    path("ecommerce/cart", view=apps_ecommerce_cart_view, name="ecommerce.cart"),
    path("ecommerce/checkout", view=apps_ecommerce_checkout_view,
         name="ecommerce.checkout"),
    path("ecommerce/sellers", view=apps_ecommerce_sellers_view,
         name="ecommerce.sellers"),
    path("ecommerce/seller-details", view=apps_ecommerce_seller_details_view,
         name="ecommerce.seller_details"),
    # Projects
    path("projects/list", view=apps_projects_list_view, name="projects.list"),
    path("projects/overview", view=apps_projects_overview_view,
         name="projects.overview"),
    path("projects/create", view=apps_projects_create_view, name="projects.create"),
    # Tasks
    path("tasks/kanban", view=apps_tasks_kanban_view, name="tasks.kanban"),
    path("tasks/list", view=apps_tasks_list_view, name="tasks.list"),
    path("tasks/details", view=apps_tasks_details_view, name="tasks.details"),
    # CRM
    path("crm/contacts", view=apps_crm_contacts_view, name="crm.contacts"),
    path("crm/companies", view=apps_crm_companies_view, name="crm.companies"),
    path("crm/deals", view=apps_crm_deals_view, name="crm.deals"),
    path("crm/leads", view=apps_crm_leads_view, name="crm.leads"),
    # Crypto
    path("crypto/transactions", view=apps_crypto_transactions_view,
         name="crypto.transactions"),
    path("crypto/buy-sell", view=apps_crypto_buy_sell_view, name="crypto.buy_sell"),
    path("crypto/orders", view=apps_crypto_orders_view, name="crypto.orders"),
    path("crypto/wallet", view=apps_crypto_wallet_view, name="crypto.wallet"),
    path("crypto/ico", view=apps_crypto_ico_view, name="crypto.ico"),
    path("crypto/kyc", view=apps_crypto_kyc_view, name="crypto.kyc"),
    # Invoices
    path("invoices/list", view=apps_invoices_list_view, name="invoices.list"),
    path("invoices/details", view=apps_invoices_details_view,
         name="invoices.details"),
    path("invoices/create", view=apps_invoices_create_view, name="invoices.create"),
    # Support Tickets
    path("support-tickets/list", view=apps_tickets_list_view, name="tickets.list"),
    path("support-tickets/details",
         view=apps_tickets_details_view, name="tickets.details"),



    path("", source, name="ecommerce.customers"),
    path('status_c/<int:source_id>/<status>/', status_c, name="status_c"),
    path('delete_source/', delete_source, name='delete_source'),
    path('sourceJs/', sourceJs, name='sourceJs'),

    path('clients/', clients, name='clients'),
    path('list_customers/', list_customer, name='list_customer'),
    path('clients/CustomerDetails/<int:customer_id>/',
         detail_customer, name='detail_customer'),

    path('delete_customer/', delete_customer, name='delete_customer'),

    path('typical_comment/<search>/',
         typical_comment, name='typical_comment'),


]
