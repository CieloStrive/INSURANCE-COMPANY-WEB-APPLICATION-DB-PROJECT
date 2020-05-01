from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.template import RequestContext
from . import models
import random, string, time
from datetime import date
import datetime
import numpy as np
from django.forms import modelformset_factory


def randString(length=10):
    # put your letters in the following string
    your_letters = '0123456789'
    return ''.join((random.choice(your_letters) for i in range(length)))


# --------------------------------Account-------------------------------------------
@login_required
def personal_center(request):
    if request.method == 'GET':
        current_user = request.user
        customer = models.Customer.objects.filter(customer_id=current_user.id)
        if customer.exists():
            # ---------update insurance status--------------
            TODAY = datetime.datetime.utcnow()
            auto = models.AutoInsurance.objects.filter(customer_id=current_user.id)
            for a in auto:
                if TODAY > a.end_date.replace(tzinfo=None):
                    models.AutoInsurance.objects.filter(insurance_id=a.insurance_id).update(insurance_status='P')
            home = models.HomeInsurance.objects.filter(customer_id=current_user.id)
            for h in home:
                if TODAY > h.end_date.replace(tzinfo=None):
                    models.HomeInsurance.objects.filter(insurance_id=h.insurance_id).update(insurance_status='P')

            # ----------update customer type----------------
            a = models.AutoInsurance.objects.filter(customer_id=current_user.id, insurance_status='C')
            h = models.HomeInsurance.objects.filter(customer_id=current_user.id, insurance_status='C')
            if a.exists() and h.exists():
                models.Customer.objects.filter(customer_id=current_user.id).update(customer_type='B')
            elif a.exists():
                models.Customer.objects.filter(customer_id=current_user.id).update(customer_type='A')
            elif h.exists():
                models.Customer.objects.filter(customer_id=current_user.id).update(customer_type='H')

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
        C_T = 'N'  # request.POST['customer_type']  # there is no POST['customer_type']
        city = request.POST['city']
        state = request.POST['state']
        if len(state) != 2:
            return render(request,'update_info.html',{'check_state':'Please input a valid state of two letters!'})
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
        messages.success(request, f'Your account has been updated!')
        return redirect('personal_center')


@login_required
def update_ins_status(request):
    #---------update insurance status--------------
    TODAY = datetime.datetime.utcnow()
    auto = models.AutoInsurance.objects.all()
    for a in auto:
        if TODAY > a.end_date.replace(tzinfo=None):
            models.AutoInsurance.objects.filter(insurance_id=a.insurance_id).update(insurance_status='P')
    home = models.HomeInsurance.objects.all()
    for h in home:
        if TODAY > h.end_date.replace(tzinfo=None):
            models.HomeInsurance.objects.filter(insurance_id=h.insurance_id).update(insurance_status='P')
    #----------update customer type----------------
    customer = models.Customer.objects.all()
    for c in customer:
        a = models.AutoInsurance.objects.filter(customer_id = c.customer_id,insurance_status='C')
        h = models.HomeInsurance.objects.filter(customer_id = c.customer_id,insurance_status='C')
        if a.exists() and h.exist():
            models.Customer.objects.filter(customer_id = c.customer_id).update(customer_type = 'B')
        elif a.exists():
            models.Customer.objects.filter(customer_id=c.customer_id).update(customer_type='A')
        elif h.exists():
            models.Customer.objects.filter(customer_id=c.customer_id).update(customer_type='H')
    return render(request, 'update_ins_status.html')


# --------------------------------Query-------------------------------------------
@login_required
def my_insurance(request):
    return render(request, 'my_insurance.html')


# --------------------------------Home Query-------------------------------------------
@login_required()
def home_query(request):
    if request.method == 'GET':
        current_user = request.user
        customer_id = current_user.id

        # show valid insurance_id
        invoice_ins = models.InvoiceHome.objects.values('insurance_id').distinct()
        a = []
        b = []
        for invoice_i in invoice_ins:
            a.append(invoice_i['insurance_id'])
        home_ins = models.HomeInsurance.objects.filter(customer_id=customer_id)
        for home in home_ins:
            b.append(home.insurance_id)
        valid_ins_id = np.intersect1d(a, b)

        error = ''
        if len(valid_ins_id) > 0:
            pass
        else:
            error = 'you have not bought any home insurance'
        return render(request, 'home_query.html', {'homes': valid_ins_id, 'error': error})

    if request.method == 'POST':
        home_id = request.POST['ins_id']
        current_user = request.user
        customer_id = current_user.id
        home_ins = models.HomeInsurance.objects.filter(insurance_id=home_id, customer_id=customer_id)
        error = ''
        home = home_ins.first()
        if home_ins.exists():
            pass
        else:
            error = 'There is no matching data'
        return render(request, 'home_result.html', {'home': home, 'error': error})  # template!!!!!!!!!


@login_required()
def house_query(request, insurance_id):
    home_record = models.HomeRecord.objects.filter(insurance_id=insurance_id)
    houses = []
    for home in home_record:
        house = models.InsuredHome.objects.filter(home_id=home.home_id).first()
        houses.append(house)
    return render(request, 'house_result.html', {'houses': houses})


# --------------------------------Auto Query-------------------------------------------
@login_required
def auto_query(request):
    if request.method == 'GET':
        current_user = request.user
        customer_id = current_user.id
        # show valid insurance_id
        invoice_ins = models.InvoiceAuto.objects.values('insurance_id').distinct()
        a = []
        b = []
        for invoice_i in invoice_ins:
            a.append(invoice_i['insurance_id'])
        auto_ins = models.AutoInsurance.objects.filter(customer_id=customer_id)
        for auto in auto_ins:
            b.append(auto.insurance_id)
        valid_ins_id = np.intersect1d(a, b)

        error = ''
        if len(valid_ins_id) > 0:
            pass
        else:
            error = 'you have not bought any auto insurance'
        return render(request, 'auto_query.html', {'autos': valid_ins_id, 'error': error})

    if request.method == 'POST':
        ins_id = request.POST['ins_id']
        current_user = request.user
        customer_id = current_user.id
        auto_ins = models.AutoInsurance.objects.filter(insurance_id=ins_id, customer_id=customer_id)
        error = ''
        auto = auto_ins.first()
        if auto_ins.exists():
            pass
        else:
            error = 'There is no matching data'
        return render(request, 'auto_result.html', {'auto': auto, 'error': error})


# vins = []


@login_required
def vehicle_query(request, insurance_id):
    request.session['i_id'] = insurance_id
    auto_record = models.AutoRecord.objects.filter(insurance_id=insurance_id)
    vehicles = []
    # global vins
    vins = []
    for auto in auto_record:
        vehicle = models.InsuredVehicle.objects.filter(vin=auto.vin).first()
        vehicles.append(vehicle)
        a = str(auto.vin)
        vins.append(a)
    request.session['vin']=vins
    return render(request, 'vehicle_result.html', {'vehicles': vehicles})


@login_required
def driver_query(request):
    # global vins
    vins = request.session.get('vin')
    i_id = request.session.get('i_id')
    drivers = []
    for vin in vins:
        vehicle_driver = models.VehicleDriver.objects.filter(vin=vin, ins_id=i_id )
        for v_driver in vehicle_driver:
            driver = models.Driver.objects.filter(license_num=v_driver.license_num).first()
            drivers.append(driver)

    return render(request, 'driver_result.html', {'drivers': drivers})


# --------------------------------Enroll-------------------------------------------
@login_required
def enroll(request):
    current_user = request.user
    customer = models.Customer.objects.filter(customer_id=current_user.id)
    if customer.exists():
        pass
    else:
        return render(request, 'error.html')
    return render(request, 'enroll.html')


# --------------------------------Installment-------------------------------------------
@login_required
def my_invoice(request):
    return render(request, 'my_invoice.html')


# --------------------------------Home Insurance-------------------------------------------
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
        request.session['premium_amount'] = premium_amount
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
        messages.success(request, f'Your successfully added a house to your current insurance plan!')
        return redirect('home_success_page')


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
        premium_amount = self.request.session.get('premium_amount')
        current_user = self.request.user
        return models.HomeRecord.objects.filter(insurance_id=ins_id)


@login_required
def invoice_home(request):
    insurance_id = request.session.get('ins_id')

    temp_id = random.randint(1, 99999999)  # be careful with range of int
    while models.InvoiceHome.objects.filter(invoice_id=temp_id):
        temp_id = random.randint(1, 99999999)

    invoice_amount = request.session.get('premium_amount')
    invoice_date = date.today()
    payment_due_date = date.today() + datetime.timedelta(days=15)

    models.InvoiceHome.objects.create(
        invoice_id=temp_id,
        insurance_id=insurance_id,
        invoice_date=invoice_date,
        payment_due_date=payment_due_date,
        invoice_amount=invoice_amount,
    )

    if request.method == 'GET':
        return render(request, 'invoice_home.html', {'insurance_id': insurance_id,
                                                     'invoice_id': temp_id,
                                                     'invoice_date': invoice_date,
                                                     'payment_due_date': payment_due_date,
                                                     'invoice_amount': invoice_amount})


@login_required()
def home_installment(request):
    total_invoice = request.session.get('premium_amount')
    num = int(float(total_invoice)/1000)
    insurance_id = request.session.get('ins_id')
    temp_id = []
    invoice_date = []
    payment_due_date = []
    invoice_amount = []

    this_temp_id = []
    this_invoice_date = []
    this_payment_due_date = []
    this_invoice_amount = []

    for i in range(num):
        t_id = random.randint(1, 99999999)
        while models.InvoiceHome.objects.filter(invoice_id=t_id) or np.intersect1d(t_id, temp_id):
            t_id = random.randint(1, 99999999)

        if (i+1)*1000 < float(total_invoice):
            i_amount = 1000.00
        else:
            i_amount = float(total_invoice) - i*1000.00

        i_date = date.today() + datetime.timedelta(days=i*30)  # pay every 30 days
        p_due_date = i_date + datetime.timedelta(days=15)
        temp_id.append(t_id)
        invoice_date.append(i_date)
        payment_due_date.append(p_due_date)
        invoice_amount.append(i_amount)
        if i == 0:
            this_temp_id.append(t_id)
            this_invoice_date.append(i_date)
            this_payment_due_date.append(p_due_date)
            this_invoice_amount.append(i_amount)

    # save model here!!!
    for i in range(num):
        models.InvoiceHome.objects.create(
            invoice_id=temp_id[i],
            insurance_id=insurance_id,
            invoice_date=invoice_date[i],
            payment_due_date=payment_due_date[i],
            invoice_amount=invoice_amount[i],
        )

    contents = []
    for i in range(num):
        contents.append({'insurance_id': insurance_id,
                         'invoice_id': temp_id[i],
                         'invoice_date': invoice_date[i],
                         'payment_due_date': payment_due_date[i],
                         'invoice_amount': invoice_amount[i]})

    this_time = []
    this_time.append({'insurance_id': insurance_id,
                      'invoice_id': this_temp_id[0],
                      'invoice_date': this_invoice_date[0],
                      'payment_due_date': this_payment_due_date[0],
                      'invoice_amount': this_invoice_amount[0]})

    context = {'contents': contents, 'thistime': this_time}

    if request.method == 'GET':
        return render(request, 'home_installment.html', context)


@login_required()
def payment_home(request, invoice_id):
    temp_id = random.randint(1, 99999999)  # be careful with range of int
    while models.PaymentHome.objects.filter(payment_id=temp_id):
        temp_id = random.randint(1, 99999999)
    payment_date = date.today()
    invoice_amount = models.InvoiceHome.objects.filter(invoice_id=invoice_id).first().invoice_amount

    if request.method == 'GET':
        return render(request, 'payment_home.html', {'invoice_id': invoice_id,
                                                     'payment_id': temp_id,
                                                     'payment_date': payment_date,
                                                     'invoice_amount': invoice_amount})

    payment_method = request.POST['payment_method']
    if request.method == 'POST':
        models.PaymentHome.objects.create(payment_id=temp_id,
                                          invoice_id=invoice_id,
                                          payment_date=payment_date,
                                          payment_method=payment_method,)
        messages.success(request, f'Your successfully paid your invoice!')
        return redirect('home_payment_success')


@login_required
def home_payment_success(request):
    if request.method == 'GET':
        return render(request, 'home_payment_success.html')
    return redirect('home_page')


@login_required()
def home_invoice_query(request):
    current_user = request.user
    customer_id = current_user.id
    # ---------------------select valid insurance id---------------------------
    invoice_ins = models.InvoiceHome.objects.values('insurance_id').distinct()
    a = []
    b = []
    for invoice_i in invoice_ins:
        a.append(invoice_i['insurance_id'])
    home_ins = models.HomeInsurance.objects.filter(customer_id=customer_id)
    for home in home_ins:
        b.append(home.insurance_id)
    valid_ins_id = np.intersect1d(a, b)

    error = ''
    # if auto_ins.exists():
    if len(valid_ins_id) != 0:
        pass
    else:
        error = 'you have not bought any home insurance'
    contents = []
    for ins_id in valid_ins_id:
        h_ins = models.HomeInsurance.objects.filter(insurance_id=ins_id).first()
        contents.append({'insurance_id': h_ins.insurance_id, 'start_date': h_ins.start_date})
    if len(contents)>1:
        contents.pop(0)
    if request.method == 'GET':
        return render(request, 'home_invoice_query.html', {'contents': contents, 'error': error})


@login_required()
def home_invoice_list(request, insurance_id):
    i_id = []
    h_records = models.InvoiceHome.objects.filter(insurance_id=insurance_id)
    for h_record in h_records:
        if models.PaymentHome.objects.filter(invoice_id=h_record.invoice_id):  # already paid
            i_id.append({'invoice_id': h_record.invoice_id,
                         'invoice_date': h_record.invoice_date,
                         'status': 'Paid'})
        else:
            i_id.append({'invoice_id': h_record.invoice_id,
                         'invoice_date': h_record.invoice_date,
                         'status': 'Unpaid'})
    if request.method == 'GET':
        return render(request, 'home_invoice_list.html', {'invoices': i_id})


# --------------------------------Home Purchase Again-------------------------------------------
@login_required
def pa_home_ins(request):
    current_user = request.user
    if request.method == 'GET':
        return render(request, 'pa_home_ins.html')
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
        request.session['premium_amount'] = premium_amount
    return redirect('pa_insured_home')


@login_required
def pa_insured_home(request):
    current_user = request.user
    if request.method == 'GET':
        return render(request, 'pa_insured_home.html')
    if request.method == 'POST':
        home_id = request.POST['home_id']

        home = models.InsuredHome.objects.filter(home_id=home_id)
        if home.exists():
            pass
        else:
            return render(request, 'pa_insured_home.html', {'check3': 'This house is not insured before! '
                                                                      'please restart enrollment for insured '
                                                                      'home and go to regular procedure '
                                                                      'for new house'})
        # session
        ins_id = request.session.get('ins_id')

        home_record = models.HomeRecord.objects.filter(home_id=home_id, insurance_id=ins_id)
        if home_record.exists():
            return render(request, 'pa_insured_home.html', {'check3': 'Please do not input repeated home!'})

        temp_id = random.randint(1, 1000000000)  # be careful with range of int
        while models.HomeRecord.objects.filter(h_r_id=temp_id):
            temp_id = random.randint(1, 1000000000)

        models.HomeRecord.objects.create(
            home=models.InsuredHome.objects.filter(home_id=home_id).first(),
            insurance=models.HomeInsurance.objects.filter(insurance_id=ins_id).first(),
            h_r_id=temp_id,
        )
        messages.success(request, f'Your successfully added a house to your current insurance plan!')
        return redirect('pa_home_success_page')


@login_required
def pa_home_success_page(request):
    if request.method == 'GET':
        return render(request, 'pa_home_success_page.html')
    return render(request, 'pa_insured_home.html')


# --------------------------------Auto Insurance-------------------------------------------
@login_required
def register_driver(request):
    if request.method == 'GET':
        return render(request, 'register_driver.html')
    if request.method == 'POST':
        license_num = request.POST['license_num']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        birthdate = request.POST['birth']
    lic = models.Driver.objects.filter(license_num=license_num)

    # if len(license_num) != 16:
    #     return render(request, 'register_driver.html', {'checkdriver': 'Invalid license length!'})

    if lic.exists():
        return render(request, 'register_driver.html', {'checkdriver': 'This driver License is registered before'})

    models.Driver.objects.create(
        license_num=license_num,
        f_name=f_name,
        l_name=l_name,
        birthdate=birthdate,
    )

    messages.success(request, 'Your successfully register a driver!')
    return render(request, 'register_driver.html')


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
            return render(request, 'insured_vehicle.html', {'check3': 'This vehicle is insured just now or before! '
                                                                      'If you want to purchase insurance '
                                                                      'for this vehicle, scroll down '
                                                                      'and click "Purchase Again"'
                                                                      'If this was not you, contact us ASAP!'})

        models.InsuredVehicle.objects.create(
            vin=vin,
            make_model_year=make_model_year,
            vehicle_status=vehicle_status,
        )
        # session
        ins_id = request.session.get('ins_id')
        temp_id = random.randint(1, 1000000000)  # be careful with range of int
        while models.AutoRecord.objects.filter(a_r_id=temp_id):
            temp_id = random.randint(1, 1000000000)

        models.AutoRecord.objects.create(
            vin=models.InsuredVehicle.objects.filter(vin=vin).first(),
            insurance=models.AutoInsurance.objects.filter(insurance_id=ins_id).first(),
            a_r_id=temp_id,
        )
        messages.success(request, 'Your successfully added a vehicle to your current insurance plan!')
        return redirect('vehicle_success_page')


@login_required
def vehicle_success_page(request):
    if request.method == 'GET':
        return render(request, 'vehicle_success_page.html')
    return render(request, 'insured_driver.html')


@login_required
def insured_driver(request):
    if request.method == 'GET':
        return render(request, 'insured_driver.html')
    if request.method == 'POST':
        license_num = request.POST['license_num']
        vin = request.session.get('vin')

        if len(license_num) < 7:
            return render(request, 'insured_driver.html', {'checklicense': 'Invalid license length: at least 7 !'})

        lic = models.Driver.objects.filter(license_num=license_num)
        if lic.exists():  # do nothing
            pass
        else:
            return render(request, 'insured_driver.html', {'checklicense': 'This driver is not registered, please register at Enroll page!'})

        i_id = request.session.get('ins_id')
        v_d = models.VehicleDriver.objects.filter(license_num=license_num, vin=vin, ins_id=i_id)
        if v_d.exists():
            return render(request, 'insured_driver.html',
                          {'checklicense': 'Please do not input repeated driver for this car!'})

        temp_id = random.randint(1, 1000000000)  # be careful with range of int
        while models.VehicleDriver.objects.filter(v_d_id=temp_id):
            temp_id = random.randint(1, 1000000000)

        models.VehicleDriver.objects.create(
            license_num=models.Driver.objects.filter(license_num=license_num).first(),
            vin=models.InsuredVehicle.objects.filter(vin=vin).first(),
            v_d_id=temp_id,
            ins_id=i_id
        )
        messages.success(request, 'Your successfully bind a driver to your current vehicle!')
        return redirect('driver_success_page')


@login_required
def driver_success_page(request):
    if request.method == 'GET':
        return render(request, 'driver_success_page.html')
    return render(request, 'insured_driver.html')


class AutoOrderListView(LoginRequiredMixin, ListView):
    model = models.AutoRecord
    template_name = 'auto_order_info.html'
    context_object_name = 'records'

    def get_queryset(self):
        # session
        ins_id = self.request.session.get('ins_id')
        premium_amount = self.request.session.get('premium_amount')
        current_user = self.request.user
        return models.AutoRecord.objects.filter(insurance_id=ins_id)


@login_required
def invoice_auto(request):
    insurance_id = request.session.get('ins_id')

    temp_id = random.randint(1, 99999999)  # be careful with range of int
    while models.InvoiceAuto.objects.filter(invoice_id=temp_id):
        temp_id = random.randint(1, 99999999)

    invoice_amount = request.session.get('premium_amount')
    invoice_date = date.today()
    payment_due_date = date.today() + datetime.timedelta(days=15)

    models.InvoiceAuto.objects.create(
        invoice_id=temp_id,
        insurance_id=insurance_id,
        invoice_date=invoice_date,
        payment_due_date=payment_due_date,
        invoice_amount=invoice_amount,
    )

    if request.method == 'GET':
        return render(request, 'invoice_auto.html', {'insurance_id': insurance_id,
                                                     'invoice_id': temp_id,
                                                     'invoice_date': invoice_date,
                                                     'payment_due_date': payment_due_date,
                                                     'invoice_amount': invoice_amount})


@login_required()
def auto_installment(request):
    total_invoice = request.session.get('premium_amount')
    num = int(float(total_invoice)/1000)
    insurance_id = request.session.get('ins_id')
    temp_id = []
    invoice_date = []
    payment_due_date = []
    invoice_amount = []

    this_temp_id = []
    this_invoice_date = []
    this_payment_due_date = []
    this_invoice_amount = []

    for i in range(num):
        t_id = random.randint(1, 99999999)
        while models.InvoiceAuto.objects.filter(invoice_id=t_id) or np.intersect1d(t_id, temp_id):
            t_id = random.randint(1, 99999999)

        if (i+1)*1000 < float(total_invoice):
            i_amount = 1000.00
        else:
            i_amount = float(total_invoice) - i*1000.00

        i_date = date.today() + datetime.timedelta(days=i*30)  # pay every 30 days
        p_due_date = i_date + datetime.timedelta(days=15)
        temp_id.append(t_id)
        invoice_date.append(i_date)
        payment_due_date.append(p_due_date)
        invoice_amount.append(i_amount)
        if i == 0:
            this_temp_id.append(t_id)
            this_invoice_date.append(i_date)
            this_payment_due_date.append(p_due_date)
            this_invoice_amount.append(i_amount)

    # save model here!!!
    for i in range(num):
        models.InvoiceAuto.objects.create(
            invoice_id=temp_id[i],
            insurance_id=insurance_id,
            invoice_date=invoice_date[i],
            payment_due_date=payment_due_date[i],
            invoice_amount=invoice_amount[i],
        )

    contents = []
    for i in range(num):
        contents.append({'insurance_id': insurance_id,
                         'invoice_id': temp_id[i],
                         'invoice_date': invoice_date[i],
                         'payment_due_date': payment_due_date[i],
                         'invoice_amount': invoice_amount[i]})

    this_time = []
    this_time.append({'insurance_id': insurance_id,
                      'invoice_id': this_temp_id[0],
                      'invoice_date': this_invoice_date[0],
                      'payment_due_date': this_payment_due_date[0],
                      'invoice_amount': this_invoice_amount[0]})

    context = {'contents': contents, 'thistime': this_time}

    if request.method == 'GET':
        return render(request, 'auto_installment.html', context)

@login_required()
def payment_auto(request, invoice_id):
    temp_id = random.randint(1, 99999999)  # be careful with range of int
    while models.PaymentAuto.objects.filter(payment_id=temp_id):
        temp_id = random.randint(1, 99999999)
    payment_date = date.today()
    invoice_amount = models.InvoiceAuto.objects.filter(invoice_id=invoice_id).first().invoice_amount

    if request.method == 'GET':
        return render(request, 'payment_auto.html', {'invoice_id': invoice_id,
                                                     'payment_id': temp_id,
                                                     'payment_date': payment_date,
                                                     'invoice_amount': invoice_amount})

    request.session['invoice_id'] = invoice_id

    if request.method == 'POST':
        payment_method = request.POST['payment_method']
        models.PaymentAuto.objects.create(payment_id=temp_id,
                                          invoice_id=request.session.get('invoice_id'),
                                          payment_date=payment_date,
                                          payment_method=payment_method,)
        messages.success(request, f'Your successfully paid your invoice!')
        return redirect('auto_payment_success')


@login_required
def auto_payment_success(request):
    if request.method == 'GET':
        return render(request, 'auto_payment_success.html')
    return redirect('home_page')

@login_required()
def auto_invoice_query(request):
    current_user = request.user
    customer_id = current_user.id
    #---------------------select valid insurance id---------------------------
    invoice_ins = models.InvoiceAuto.objects.values('insurance_id').distinct()
    a = []
    b = []
    for invoice_i in invoice_ins:
        a.append(invoice_i['insurance_id'])
    auto_ins = models.AutoInsurance.objects.filter(customer_id=customer_id)
    for auto in auto_ins:
        b.append(auto.insurance_id)
    valid_ins_id = np.intersect1d(a, b)

    error = ''
    #if auto_ins.exists():
    if len(valid_ins_id) != 0:
        pass
    else:
        error = 'you have not bought any auto insurance'
    contents = []
    for ins_id in valid_ins_id:
        a_ins = models.AutoInsurance.objects.filter(insurance_id=ins_id).first()
        contents.append({'insurance_id': a_ins.insurance_id, 'start_date': a_ins.start_date})

    if len(contents) > 1:
        contents.pop(0)
    if request.method == 'GET':
        return render(request, 'auto_invoice_query.html', {'contents': contents, 'error': error})


@login_required()
def auto_invoice_list(request, insurance_id):
    i_id = []
    a_records = models.InvoiceAuto.objects.filter(insurance_id=insurance_id)
    for a_record in a_records:
        if models.PaymentAuto.objects.filter(invoice_id=a_record.invoice_id):  # already paid
            i_id.append({'invoice_id': a_record.invoice_id,
                         'invoice_date': a_record.invoice_date,
                         'status': 'Paid'})
        else:
            i_id.append({'invoice_id': a_record.invoice_id,
                         'invoice_date': a_record.invoice_date,
                         'status': 'Unpaid'})
    if request.method == 'GET':
        return render(request, 'auto_invoice_list.html', {'invoices': i_id})


# --------------------------------Auto Purchase Again-------------------------------------------
def pa_auto_ins(request):
    current_user = request.user
    if request.method == 'GET':
        return render(request, 'pa_auto_ins.html')
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
    return redirect('pa_insured_vehicle')


def pa_insured_vehicle(request):
    current_user = request.user
    if request.method == 'GET':
        return render(request, 'pa_insured_vehicle.html')
    if request.method == 'POST':
        vin = request.POST['vin']
        # use session
        request.session['vin'] = vin

        vehicle = models.InsuredVehicle.objects.filter(vin=vin)
        if vehicle.exists():
            pass
        else:
            return render(request, 'pa_insured_vehicle.html', {'check3': 'This vehicle is not insured before, '
                                                                         'please restart enrollment for insured '
                                                                         'vehicle and go to regular procedure '
                                                                         'for new vehicle'})

        # session
        ins_id = request.session.get('ins_id')

        auto_record = models.AutoRecord.objects.filter(vin=vin, insurance_id=ins_id)
        if auto_record.exists():
            return render(request, 'pa_insured_vehicle.html', {'check3': 'Please do not input repeated vehicle!'})

        temp_id = random.randint(1, 1000000000)  # be careful with range of int
        while models.AutoRecord.objects.filter(a_r_id=temp_id):
            temp_id = random.randint(1, 1000000000)

        models.AutoRecord.objects.create(
            vin = models.InsuredVehicle.objects.filter(vin=vin).first(),
            insurance = models.AutoInsurance.objects.filter(insurance_id=ins_id).first(),
            a_r_id = temp_id,
        )
        messages.success(request, 'Your successfully added a vehicle to your current insurance plan!')
        return redirect('pa_vehicle_success_page')


def pa_vehicle_success_page(request):
    if request.method == 'GET':
        return render(request, 'pa_vehicle_success_page.html')
    return render(request, 'pa_insured_driver.html')


@login_required
def pa_insured_driver(request):
    if request.method == 'GET':
        return render(request, 'pa_insured_driver.html')
    if request.method == 'POST':
        license_num = request.POST['license_num']
        vin = request.session.get('vin')

        if len(license_num) != 16:
            return render(request, 'pa_insured_driver.html', {'checklicense': 'Invalid license length!'})

        lic = models.Driver.objects.filter(license_num=license_num)
        if lic.exists():  # do nothing
            pass
        else:
            return render(request, 'pa_insured_driver.html', {'checklicense': 'license is not registered, '
                                                                              'please register at Enroll page!'})

        i_id = request.session.get('ins_id')
        v_d = models.VehicleDriver.objects.filter(license_num=license_num, vin=vin, ins_id=i_id)
        if v_d.exists():
            return render(request, 'pa_insured_driver.html',
                          {'checklicense': 'Please do not input repeated driver for this car!'})

        temp_id = random.randint(1, 1000000000)  # be careful with range of int
        while models.VehicleDriver.objects.filter(v_d_id=temp_id):
            temp_id = random.randint(1, 1000000000)

        models.VehicleDriver.objects.create(
            license_num=models.Driver.objects.filter(license_num=license_num).first(),
            vin=models.InsuredVehicle.objects.filter(vin=vin).first(),
            v_d_id=temp_id,
            ins_id=i_id
        )
        messages.success(request, 'Your successfully bind a driver to your current vehicle!')
        return redirect('pa_driver_success_page')


@login_required
def pa_driver_success_page(request):
    if request.method == 'GET':
        return render(request, 'pa_driver_success_page.html')
    return render(request, 'pa_insured_driver.html')
