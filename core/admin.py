from django.contrib import admin
from core.models import Vehicle, Supply, Provider, Maintenance, Traffic
# Register your models here.

@admin.register(Vehicle)
class ModelAdminVehicle(admin.ModelAdmin):
    list_display = ("brand", "vehicle", "color", "plate", "date_create")
    list_filter = ("plate", "vehicle")
    search_fields = ('plate', 'vehicle', 'brand')


@admin.register(Maintenance)
class ModelAdminMaintenance(admin.ModelAdmin):
    list_display = ("service", "provider", "vehicle", "mark_main", "departure_date")
    list_filter = ("service", "vehicle", "provider")
    search_fields = ('vehicle', 'vehicle')
    
@admin.register(Provider)
class ModelAdminProvider(admin.ModelAdmin):
    list_display = ("provide_name", "address", "number", "district", "city", "phone_number", "email", "date_create")
    list_filter = ("provide_name", "city", "email", "address")
    search_fields = ("provide_name", "city", "phone_number")


@admin.register(Traffic)
class ModelAdminTraffic(admin.ModelAdmin):
    list_display = ('vehicle', 'mark_traffic', 'departure_date', 'departure_time', 'km_of_exit', 'destiny', 'arrival_date', 'arrival_time', 'arrival_kml', 'service_purpose', 'drivers_name', 'asked_by', 'diferenca')
    list_filter = ('vehicle', 'destiny', 'departure_date', 'arrival_date')
    search_fields = ('vehicle', 'destiny', 'drivers_name')
    #autocomplete_fields = ['difference']


@admin.register(Supply)
class ModelAdminSupply(admin.ModelAdmin):
    list_display = ('date_supply', 'amount_ofag_liters', 'milee', 'supply_value', 'payment', 'driver_name', 'vehicle', 'mark_supply')
    list_filter = ('date_supply', 'payment', 'driver_name', 'vehicle')
    search_fields = ('date_supply', 'payment', 'vehicle', 'driver_name')






