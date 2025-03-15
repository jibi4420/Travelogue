from django.contrib import admin
from .models import TourPackage, Booking, Payment, Refund

admin.site.register(TourPackage)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Refund)


# Register your models here.
