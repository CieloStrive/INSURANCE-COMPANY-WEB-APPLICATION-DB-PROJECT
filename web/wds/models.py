# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

#--------------------------- add index with 'db_index=True' -------------------------------------

class AutoInsurance(models.Model):
    insurance_id = models.CharField(db_index=True, primary_key=True, max_length=10)
    customer = models.ForeignKey('Customer', models.DO_NOTHING, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)
    insurance_status = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'auto_insurance'

    def __str__(self):
        return self.insurance_id


class AutoRecord(models.Model):
    vin = models.ForeignKey('InsuredVehicle', models.DO_NOTHING, db_column='vin')
    insurance = models.ForeignKey(AutoInsurance, models.DO_NOTHING)
    a_r_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'auto_record'


class Customer(models.Model):
    customer_id = models.IntegerField(db_index=True, primary_key=True)
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
        managed = False
        db_table = 'customer'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Driver(models.Model):
    license_num = models.CharField(db_index=True, primary_key=True, max_length=16)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    birthdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'driver'

    def __str__(self):
        return self.license_num


class HomeInsurance(models.Model):
    insurance_id = models.CharField(db_index=True, primary_key=True, max_length=10)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)
    insurance_status = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'home_insurance'

    def __str__(self):
        return self.insurance_id


class HomeRecord(models.Model):
    home = models.ForeignKey('InsuredHome', models.DO_NOTHING)
    insurance = models.ForeignKey(HomeInsurance, models.DO_NOTHING)
    h_r_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'home_record'


class InsuredHome(models.Model):
    home_id = models.BigIntegerField(db_index=True, primary_key=True)
    home_purchase_date = models.DateTimeField()
    home_purchase_value = models.DecimalField(max_digits=10, decimal_places=2)
    home_area = models.IntegerField()
    home_type = models.CharField(max_length=1)
    auto_fire_notification = models.IntegerField()
    home_security_system = models.IntegerField()
    swimming_pool = models.CharField(max_length=1, blank=True, null=True)
    basement = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'insured_home'


class InsuredVehicle(models.Model):
    vin = models.CharField(db_index=True, primary_key=True, max_length=17)
    make_model_year = models.SmallIntegerField()
    vehicle_status = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'insured_vehicle'

    def __str__(self):
        return self.vin


class InvoiceAuto(models.Model):
    invoice_id = models.IntegerField(db_index=True, primary_key=True)
    insurance = models.ForeignKey(AutoInsurance, models.DO_NOTHING)
    invoice_date = models.DateTimeField()
    payment_due_date = models.DateTimeField()
    invoice_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'invoice_auto'


class InvoiceHome(models.Model):
    invoice_id = models.IntegerField(db_index=True, primary_key=True)
    insurance = models.ForeignKey(HomeInsurance, models.DO_NOTHING)
    invoice_date = models.DateTimeField()
    payment_due_date = models.DateTimeField()
    invoice_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'invoice_home'


class PaymentAuto(models.Model):
    payment_id = models.IntegerField(db_index=True, primary_key=True)
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=6)
    invoice = models.OneToOneField(InvoiceAuto, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_auto'


class PaymentHome(models.Model):
    payment_id = models.IntegerField(db_index=True, primary_key=True)
    invoice = models.OneToOneField(InvoiceHome, models.DO_NOTHING, blank=True, null=True)
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'payment_home'


class VehicleDriver(models.Model):
    license_num = models.ForeignKey(Driver, models.DO_NOTHING, db_column='license_num')
    vin = models.ForeignKey(InsuredVehicle, models.DO_NOTHING, db_column='vin')
    v_d_id = models.IntegerField(primary_key=True)
    ins_id = models.CharField(db_index=True, max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_driver'
