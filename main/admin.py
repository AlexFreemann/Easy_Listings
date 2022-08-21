from django.contrib import admin
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class AccountInline(admin.StackedInline):
    model = Account
    can_delete =False
    verbose_name_plural = 'Accounts'


class CustomUserAdmin (UserAdmin):
    inlines = (AccountInline,)
    list_display = ('username','shop_name','shop_connection','paid','verified')

    def shop_name(self, obj):
        return obj.account.shop_name

    def shop_connection(self, obj):
        return obj.account.shop_connection

    def paid(self, obj):
        return obj.account.paid

    def verified(self, obj):
        return obj.account.verified

admin.site.unregister(User)
admin.site.register(User,CustomUserAdmin)

admin.site.register(Account)

