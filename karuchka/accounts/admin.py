from django.contrib import admin

from karuchka.accounts.models import Profile



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
