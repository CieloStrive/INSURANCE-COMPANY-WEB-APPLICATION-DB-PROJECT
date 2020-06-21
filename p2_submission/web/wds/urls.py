"""product_hunt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
urlpatterns = [
    # --------------------------------Account-------------------------------------------
    path('personal_center/', views.personal_center, name='personal_center'),
    path('personal_center/update', views.update_info, name='update_info'),
    path('personal_center/update_ins_status', views.update_ins_status, name='update_ins_status'),
    path('personal_center/delete_ins', views.delete_ins, name='delete_ins'),
    path('personal_center/delete_confirm', views.delete_confirm, name='delete_confirm'),
    path('personal_center/delete/<str:ins_id>', views.delete, name='delete'),

    # --------------------------------Query-------------------------------------------
    path('personal_center/myinsurance', views.my_insurance, name='my_insurance'),
    path('personal_center/myinsurance/auto_query', views.auto_query, name='auto_query'),
    path('personal_center/myinsurance/vehicle_query/<str:insurance_id>', views.vehicle_query, name='vehicle_query'),
    path('personal_center/myinsurance/driver_query', views.driver_query, name='driver_query'),
    path('personal_center/myinsurance/home_query', views.home_query, name='home_query'),
    path('personal_center/myinsurance/house_query/<str:insurance_id>', views.house_query, name='house_query'),

    # --------------------------------Enroll-------------------------------------------
    path('enroll/', views.enroll, name='enroll'),

    # ---------------------- -----Invoice & Payment-------------------------------------------
    path('personal_center/myinvoice', views.my_invoice, name='my_invoice'),
    path('personal_center/myinvoice/home_invoice_query', views.home_invoice_query, name='home_invoice_query'),
    path('personal_center/myinvoice/home_invoice_list/<str:insurance_id>', views.home_invoice_list, name='home_invoice_list'),
    path('personal_center/myinvoice/auto_invoice_query', views.auto_invoice_query, name='auto_invoice_query'),
    path('personal_center/myinvoice/auto_invoice_list/<str:insurance_id>', views.auto_invoice_list, name='auto_invoice_list'),

    # --------------------------------Home-------------------------------------------
    path('enroll/home_ins', views.home_ins, name='home_ins'),
    path('enroll/insured_home', views.insured_home, name='insured_home'),
    path('enroll/home_success_page', views.home_success_page, name='home_success_page'),
    path('enroll/home_order_info', views.HomeOrderListView.as_view(), name='home_order_info'),
    path('enroll/invoice_home', views.invoice_home, name='invoice_home'),
    path('enroll/payment_home/<int:invoice_id>', views.payment_home, name='payment_home'),
    path('enroll/home_installment', views.home_installment, name='home_installment'),
    path('enroll/home_payment_success', views.home_payment_success, name='home_payment_success'),

    # --------------------------------Auto-------------------------------------------
    path('enroll/auto_ins', views.auto_ins, name='auto_ins'),
    path('enroll/insured_vehicle', views.insured_vehicle, name='insured_vehicle'),
    path('enroll/vehicle_success_page', views.vehicle_success_page, name='vehicle_success_page'),
    path('enroll/insured_driver', views.insured_driver, name='insured_driver'),
    path('enroll/driver_success_page', views.driver_success_page, name='driver_success_page'),
    path('enroll/register_driver', views.register_driver, name='register_driver'),
    path('enroll/auto_order_info', views.AutoOrderListView.as_view(), name='auto_order_info'),
    path('enroll/invoice_auto', views.invoice_auto, name='invoice_auto'),
    path('enroll/payment_auto/<int:invoice_id>', views.payment_auto, name='payment_auto'),
    path('enroll/auto_installment', views.auto_installment, name='auto_installment'),
    path('enroll/auto_payment_success', views.auto_payment_success, name='auto_payment_success'),

    # --------------------------------Purchase Again Auto-------------------------------------------
    path('enroll/pa_auto_ins', views.pa_auto_ins, name='pa_auto_ins'),
    path('enroll/pa_insured_vehicle', views.pa_insured_vehicle, name='pa_insured_vehicle'),
    path('enroll/pa_vehicle_success_page', views.pa_vehicle_success_page, name='pa_vehicle_success_page'),
    path('enroll/pa_insured_driver', views.pa_insured_driver, name='pa_insured_driver'),
    path('enroll/pa_driver_success_page', views.pa_driver_success_page, name='pa_driver_success_page'),

    # --------------------------------Purchase Again Home-------------------------------------------
    path('enroll/pa_home_ins', views.pa_home_ins, name='pa_home_ins'),
    path('enroll/pa_insured_home', views.pa_insured_home, name='pa_insured_home'),
    path('enroll/pa_home_success_page', views.pa_home_success_page, name='pa_home_success_page'),
]
