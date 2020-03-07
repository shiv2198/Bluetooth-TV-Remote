from django.contrib import admin
from .models import Distributor,Channel,Show,Time,Customer
# Register your models here.
admin.site.register(Distributor)
admin.site.register(Channel)
admin.site.register(Show)
admin.site.register(Time)
admin.site.register(Customer)

