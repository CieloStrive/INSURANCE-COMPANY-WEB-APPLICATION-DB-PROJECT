from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import models
import random, string
import datetime

def randString(length=10):
    # put your letters in the following string
    your_letters = '0123456789'
    return ''.join((random.choice(your_letters) for i in range(length)))


@login_required
def personal_center(request):
    if request.method == 'GET':
        current_user = request.user
        customer = models.Customer.objects.filter(customer_id=current_user.id)
        if customer.exists():
            return render(request, 'personal_center.html', {'customer': customer.first()})
        else:
            return redirect('update_info')


def update_info(request):
    current_user = request.user
    customer = models.Customer.objects.filter(customer_id=current_user.id)
    if request.method == 'GET':
        if customer.exists():
            return render(request, 'update_info.html', {'customer': customer.first()})
        return render(request, 'update_info.html')
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        gender = request.POST['gender']
        M_S = request.POST['M_S']
        C_T = request.POST['C_T']
        city = request.POST['city']
        state = request.POST['state']
        street = request.POST['street']
        zip = request.POST['zip']
        if customer.exists():
            models.Customer.objects.filter(customer_id=current_user.id).update(
                first_name=f_name,
                last_name=l_name,
                gender=gender,
                marital_status=M_S,
                customer_type=C_T,
                city=city,
                state=state,
                street=street,
                zip=zip,
            )
        else:
            models.Customer.objects.create(
                customer_id=current_user.id,
                first_name=f_name,
                last_name=l_name,
                gender=gender,
                marital_status=M_S,
                customer_type=C_T,
                city=city,
                state=state,
                street=street,
                zip=zip,
            )
        return redirect('personal_center')


@login_required
def enroll(request):
    return render(request, 'enroll.html')


@login_required
def home_ins(request):
    # current_user = request.user
    if request.method == 'GET':
        # today = datetime.date.today()
        return render(request, 'home_ins.html')
    if request.method == 'POST':
        current_user = request.user
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        premium_amount = request.POST['premium_amount']
        temp_id = randString(10)
        while models.HomeInsurance.objects.filter(insurance_id=temp_id) or \
                models.AutoInsurance.objects.filter(insurance_id=temp_id):
            temp_id = randString(10)

        models.HomeInsurance.objects.create(
            insurance_id=temp_id,  # need to be modified later
            customer_id=current_user.id,
            start_date=start_date,
            end_date=end_date,
            premium_amount=premium_amount,
            insurance_status='C',  # need to be modified later
        )
    return redirect('insured_home')


@login_required
def insured_home(request):
    current_user = request.user
    if request.method == 'GET':
        return render(request, 'insured_home.html')
    if request.method == 'POST':
        home_id = request.POST['home_id']
        home_purchase_date = request.POST['home_purchase_date']
        home_purchase_value = request.POST['home_purchase_value']
        home_area = request.POST['home_area']
        home_type = request.POST['home_type']
        auto_fire_notification = request.POST['auto_fire_notification']
        home_security_system = request.POST['home_security_system']

        if request.POST['swimming_pool'] == "N":
            swimming_pool = None
        else:
            swimming_pool = request.POST['swimming_pool']

        basement = request.POST['basement']

        home = models.InsuredHome.objects.filter(home_id=home_id)
        if home.exists():
            return render(request, 'insured_home.html', {'check3': 'This house is already insured! '
                                                                   'If you want to purchase another insurance '
                                                                   'for this house, scroll down '
                                                                   'and click "Purchase Again"'})

        models.InsuredHome.objects.create(
            home_id=home_id,
            home_purchase_date=home_purchase_date,
            home_purchase_value=home_purchase_value,
            home_area=home_area,
            home_type=home_type,
            auto_fire_notification=auto_fire_notification,
            home_security_system=home_security_system,
            swimming_pool=swimming_pool,
            basement=basement,
        )
        return redirect('home_record')


@login_required
def home_record(request):
    if request.method == 'GET':
        return render(request, 'home_record.html')


@login_required
def auto_ins(request):
    current_user = request.user
    if request.method == 'GET':
        return render(request, 'auto_ins.html')
    if request.method == 'POST':
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        premium_amount = request.POST['premium_amount']
        temp_id = randString(10)
        while models.HomeInsurance.objects.filter(insurance_id=temp_id) or \
                models.AutoInsurance.objects.filter(insurance_id=temp_id):
            temp_id = randString(10)

        models.AutoInsurance.objects.create(
            insurance_id=temp_id,  # need to be modified later
            customer_id=current_user.id,
            start_date=start_date,
            end_date=end_date,
            premium_amount=premium_amount,
            insurance_status='C',  # need to be modified later
        )
    return redirect('insured_vehicle')

@login_required
def insured_vehicle(request):
    current_user = request.user
    if request.method == 'GET':
        return render(request, 'insured_vehicle.html')
    # if request.method == 'POST':
    #     home_id = request.POST['home_id']
    #     home_purchase_date = request.POST['home_purchase_date']
    #     home_purchase_value = request.POST['home_purchase_value']
    #     home_area = request.POST['home_area']
    #     home_type = request.POST['home_type']
    #     auto_fire_notification = request.POST['auto_fire_notification']
    #     home_security_system = request.POST['home_security_system']
    #
    #     if request.POST['swimming_pool'] == "N":
    #         swimming_pool = None
    #     else:
    #         swimming_pool = request.POST['swimming_pool']
    #
    #     basement = request.POST['basement']
    #
    #     home = models.InsuredHome.objects.filter(home_id=home_id)
    #     if home.exists():
    #         return render(request, 'insured_home.html', {'check3': 'This house is already insured! '
    #                                                                'If you want to purchase another insurance '
    #                                                                'for this house, scroll down '
    #                                                                'and click "Purchase Again"'})
