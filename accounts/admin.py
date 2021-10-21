from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from accounts.models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active')
    # fields linked to the Details page
    list_display_links = ('email', 'username', 'first_name', 'last_name')
    # read-only
    readonly_fields = ('last_login', 'date_joined')
    # inverse ordering
    ordering = ('-date_joined',)
    # require
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
