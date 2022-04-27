from django.contrib import admin

from karuchka.accounts.models import Profile



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # inlines = (VehicleInlineAdmin, )
    list_display = ('first_name', 'last_name')
    # list_filter = ('is_staff', 'is_superuser', 'groups')
    # ordering = ('email',)
    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     ('Permissions', {
    #         'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
    #     }),
    #     ('Important dates', {'fields': ('last_login', 'date_joined')}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2'),
    #     }),
    # )
    # readonly_fields = ('date_joined',)