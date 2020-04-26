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
    path('personal_center/', views.personal_center, name='personal_center'),
    path('personal_center/update', views.update_info, name='update_info'),

    path('enroll/', views.enroll, name='enroll'),

    path('enroll/home_ins', views.home_ins, name='home_ins'),
    path('enroll/insured_home', views.insured_home, name='insured_home'),
    path('enroll/home_success_page', views.home_success_page, name='home_success_page'),
    path('enroll/home_order_info', views.HomeOrderListView.as_view(), name='home_order_info'),
    path('enroll/payment_home', views.payment_home, name='payment_home'),
    #path('enroll/example', views.insured_home, name='example'),

    path('enroll/auto_ins', views.auto_ins, name='auto_ins'),
    path('enroll/insured_vehicle', views.insured_vehicle, name='insured_vehicle'),
    path('enroll/vehicle_success_page', views.vehicle_success_page, name='vehicle_success_page'),
    path('enroll/insured_driver', views.insured_driver, name='insured_driver'),
    path('enroll/driver_success_page', views.driver_success_page, name='driver_success_page'),
    path('enroll/auto_order_info', views.AutoOrderListView, name='auto_order_info'),
    path('enroll/register_driver', views.register_driver, name='register_driver'),

]
