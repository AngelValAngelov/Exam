from django.contrib import admin

from karuchka.main.models import Vehicle


class VehicleInlineAdmin(admin.StackedInline):
    model = Vehicle




@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model')


