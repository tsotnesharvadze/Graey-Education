from django.contrib import admin

from wash.models import CarType, WashType, Coupon, Order, Car


@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,
         {
             'fields': ('name', 'price')
         }
         ),
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('price',)


admin.site.register([WashType, Coupon, Car])
