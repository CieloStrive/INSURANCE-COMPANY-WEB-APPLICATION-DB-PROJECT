from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from . import models
import random, string
from django.forms import modelformset_factory


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
        C_T = 'H'  # request.POST['customer_type']  # there is no POST['customer_type']
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
        messages.success(request, 'Your account has been updated!')
        return redirect('personal_center')


@login_required
def enroll(request):
    return render(request, 'enroll.html')


@login_required
def home_ins(request):
    current_user = request.user
    if request.method == 'GET':
        return render(request, 'home_ins.html')
    if request.method == 'POST':
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
        # use session
        request.session['ins_id'] = temp_id  # 不能在insured_home筛选最大的id来传递id建立record，多用户同时使用出错
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

        # use session
        request.session['home_id'] = home_id

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
        # session
        ins_id = request.session.get('ins_id')
        temp_id = random.randint(1, 1000000000)  # be careful with range of int
        while models.HomeRecord.objects.filter(h_r_id=temp_id):
            temp_id = random.randint(1, 1000000000)

        models.HomeRecord.objects.create(
            home=models.InsuredHome.objects.filter(home_id=home_id).first(),
            insurance=models.HomeInsurance.objects.filter(insurance_id=ins_id).first(),
            h_r_id=temp_id,
        )
        messages.success(request, 'Your successfully added a house to your current insurance plan!')
        return redirect('home_success_page')


# @login_required
# def insured_home(request):
#     #current_user = request.user
#     InsuredHomeFormSet = modelformset_factory(models.InsuredHome, fields=('home_id',
#                                                                           'home_purchase_date',
#                                                                           'home_purchase_value',
#                                                                           'home_area',
#                                                                           'home_type',
#                                                                           'auto_fire_notification',
#                                                                           'home_security_system',
#                                                                           'swimming_pool',
#                                                                           'basement'), extra=2)
#     if request.method == 'POST':
#         form = InsuredHomeFormSet(request.POST)
#         ins = form.save()
#     form = InsuredHomeFormSet(queryset=models.InsuredHome.objects.none())
#     return render(request, 'example.html', {'form': form})


# @login_required
# def home_review(request):
#     if request.method == 'GET':
#         current_user = request.user
#         #home = models.InsuredHome.objects.filter(home_id=home_id)
#         return render(request, 'home_review.html')


@login_required
def home_success_page(request):
    if request.method == 'GET':
        return render(request, 'home_success_page.html')
    return render(request, 'insured_home.html')


class HomeOrderListView(LoginRequiredMixin, ListView):
    model = models.HomeRecord
    template_name = 'home_order_info.html'
    context_object_name = 'records'

    def get_queryset(self):
        # session
        ins_id = self.request.session.get('ins_id')
        current_user = self.request.user
        return models.HomeRecord.objects.filter(insurance_id=ins_id)

@login_required
def payment_home(request):
    if request.method == 'GET':
        return render(request, 'payment_home.html')


#########################################Auto Insurance##################################################


@login_required
def register_driver(request):
    if request.method == 'GET':
        return render(request,'register_driver.html')
    if request.method == 'POST':
        license_num = request.POST['license_num']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        birthdate = request.POST['birth']
    lic = models.Driver.objects.filter(license_num=license_num)

    if len(license_num) != 16:
        return render(request, 'register_driver.html', {'checkdriver': 'Invalid license length!'})

    if lic.exists():
        return render(request, 'register_driver.html', {'checkdriver': 'This driver License is registered before'})

    models.Driver.objects.create(
        license_num = license_num,
        f_name = f_name,
        l_name = l_name,
        birthdate = birthdate,
    )

    messages.success(request, 'Your successfully register a driver!')
    return render(request,'register_driver.html')

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
        # use session
        request.session['ins_id'] = temp_id
    return redirect('insured_vehicle')

@login_required
def insured_vehicle(request):
    current_user = request.user
    if request.method == 'GET':
        return render(request, 'insured_vehicle.html')
    if request.method == 'POST':
        vin = request.POST['vin']
        make_model_year = request.POST['make_model_year']
        vehicle_status = request.POST['vehicle_status']

        # use session
        request.session['vin'] = vin

        vehicle = models.InsuredVehicle.objects.filter(vin=vin)
        if vehicle.exists():
            return render(request, 'insured_vehicle.html', {'check3': 'This vehicle is insured/registered before! '
                                                                   'If you want to purchase insurance '
                                                                   'for this vehicle, scroll down '
                                                                   'and click "Purchase Again"'
                                                                   'If this was not you, contact us ASAP!'})

        models.InsuredVehicle.objects.create(
            vin = vin,
            make_model_year = make_model_year,
            vehicle_status = vehicle_status,

        )
        # session
        ins_id = request.session.get('ins_id')
        temp_id = random.randint(1, 1000000000)  # be careful with range of int
        while models.AutoRecord.objects.filter(a_r_id=temp_id):
            temp_id = random.randint(1, 1000000000)
        models.AutoRecord.objects.create(
            vin = models.InsuredVehicle.objects.filter(vin=vin).first(),
            insurance = models.AutoInsurance.objects.filter(insurance_id=ins_id).first(),
            a_r_id = temp_id,
        )
        messages.success(request, 'Your successfully added a vehicle to your current insurance plan!')
        return redirect('vehicle_success_page')

@login_required
def vehicle_success_page(request):
    if request.method == 'GET':
        return render(request, 'vehicle_success_page.html')
    return render(request, 'insured_driver.html')

def insured_driver(request):
    if request.method == 'GET':
        return render(request,'insured_driver.html')
    if request.method == 'POST':
        license_num = request.POST['license_num']
        vin = request.session.get('vin')

        if len(license_num) != 16:
            return render(request,'insured_driver.html',{'checklicense':'Invalid license length!'})

        lic = models.Driver.objects.filter(license_num=license_num)
        if lic.exists(): #do nothing
            pass
        else:
            return render(request, 'insured_driver.html', {'checklicense': 'license is not registered, please register at Enroll page!'})

        temp_id = random.randint(1, 1000000000)  # be careful with range of int
        while models.VehicleDriver.objects.filter(v_d_id=temp_id):
            temp_id = random.randint(1, 1000000000)

        models.VehicleDriver.objects.create(
            license_num = models.Driver.objects.filter(license_num=license_num).first(),
            vin = models.InsuredVehicle.objects.filter(vin=vin).first(),
            v_d_id=temp_id,
        )
        messages.success(request, 'Your successfully bind a driver to your current vehicle!')
        return redirect('driver_success_page')

@login_required
def driver_success_page(request):
    if request.method == 'GET':
        return render(request, 'driver_success_page.html')
    return render(request, 'insured_driver.html')

@login_required
def AutoOrderListView(request):
    return render(request,'auto_order_info.html')