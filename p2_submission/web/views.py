from django.shortcuts import render
from .wds import models

# Create your views here.

def home (request):
    current_user = request.user
    customer = models.Customer.objects.filter(customer_id=current_user.id).first()
    print(customer,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    return render(request,'home.html',{'sid':customer.first_name})