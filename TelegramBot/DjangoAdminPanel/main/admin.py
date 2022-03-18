from django.contrib import admin

# Register your models here.
from DjangoAdminPanel.main.models import User, Referral


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'name', 'balance', 'address')

@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('user', 'referrer')