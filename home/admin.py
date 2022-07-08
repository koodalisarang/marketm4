from django.contrib import admin

# Register your models here.
from home.models import register, stokein, busket, order, amount

admin.site.register(register)
admin.site.register(stokein)
admin.site.register(busket)
admin.site.register(order)
admin.site.register(amount)

