# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AutoInsurance(models.Model):
    insurance_id = models.CharField(primary_key=True, max_length=10)
    customer = models.ForeignKey('Customer', models.DO_NOTHING, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)
    insurance_status = models.CharField(max_length=1)

    class Meta:
        # managed = False
        db_table = 'auto_insurance'


class AutoRecord(models.Model):
    vin = models.ForeignKey('InsuredVehicle', models.DO_NOTHING, db_column='vin', primary_key=True)
    insurance = models.ForeignKey(AutoInsurance, models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'auto_record'
        unique_together = (('vin', 'insurance'),)


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, blank=True, null=True)
    marital_status = models.CharField(max_length=1)
    customer_type = models.CharField(max_length=2)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    street = models.CharField(max_length=30)
    zip = models.CharField(max_length=5)

    class Meta:
        # managed = False
        db_table = 'customer'


class Driver(models.Model):
    license_num = models.CharField(primary_key=True, max_length=16)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    birthdate = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'driver'


class HomeInsurance(models.Model):
    insurance_id = models.CharField(primary_key=True, max_length=10)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)
    insurance_status = models.CharField(max_length=1)

    class Meta:
        # managed = False
        db_table = 'home_insurance'


class HomeRecord(models.Model):
    home = models.ForeignKey('InsuredHome', models.DO_NOTHING, primary_key=True)
    insurance = models.ForeignKey(HomeInsurance, models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'home_record'
        unique_together = (('home', 'insurance'),)


class InsuredHome(models.Model):
    home_id = models.BigIntegerField(primary_key=True)
    home_purchase_date = models.DateTimeField()
    home_purchase_value = models.DecimalField(max_digits=10, decimal_places=2)
    home_area = models.IntegerField()
    home_type = models.CharField(max_length=1)
    auto_fire_notification = models.IntegerField()
    home_security_system = models.IntegerField()
    swimming_pool = models.CharField(max_length=1, blank=True, null=True)
    basement = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'insured_home'


class InsuredVehicle(models.Model):
    vin = models.CharField(primary_key=True, max_length=17)
    make_model_year = models.SmallIntegerField()
    vehicle_status = models.CharField(max_length=1)

    class Meta:
        # managed = False
        db_table = 'insured_vehicle'


class InvoiceAuto(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    insurance = models.ForeignKey(AutoInsurance, models.DO_NOTHING)
    invoice_date = models.DateTimeField()
    payment_due_date = models.DateTimeField()
    invoice_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        # managed = False
        db_table = 'invoice_auto'


class InvoiceHome(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    insurance = models.ForeignKey(HomeInsurance, models.DO_NOTHING)
    invoice_date = models.DateTimeField()
    payment_due_date = models.DateTimeField()
    invoice_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        # managed = False
        db_table = 'invoice_home'


class PaymentAuto(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=6)
    invoice = models.ForeignKey(InvoiceAuto, models.DO_NOTHING, unique=True, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'payment_auto'


class PaymentHome(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    invoice = models.ForeignKey(InvoiceHome, models.DO_NOTHING, unique=True, blank=True, null=True)
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=6)

    class Meta:
        # managed = False
        db_table = 'payment_home'


class VehicleDriver(models.Model):
    license_num = models.ForeignKey(Driver, models.DO_NOTHING, db_column='license_num', primary_key=True)
    vin = models.ForeignKey(InsuredVehicle, models.DO_NOTHING, db_column='vin')

    class Meta:
        # managed = False
        db_table = 'vehicle_driver'
        unique_together = (('license_num', 'vin'),)
