from django.contrib import admin
# Register your models here.

from .models import Customer

from .models import HomeInsurance
from .models import HomeRecord
from .models import InsuredHome
from .models import InvoiceHome
from .models import PaymentHome

from .models import AutoInsurance
from .models import AutoRecord
from .models import InsuredVehicle
from .models import VehicleDriver
from .models import Driver
from .models import InvoiceAuto
from .models import PaymentAuto

admin.site.register(Customer)
admin.site.register(HomeInsurance)
admin.site.register(HomeRecord)
admin.site.register(InsuredHome)
admin.site.register(InvoiceHome)
admin.site.register(PaymentHome)
admin.site.register(AutoInsurance)
admin.site.register(AutoRecord)
admin.site.register(InsuredVehicle)
admin.site.register(VehicleDriver)
admin.site.register(Driver)
admin.site.register(InvoiceAuto)
admin.site.register(PaymentAuto)

