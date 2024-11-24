# application/admin.py

# from django.contrib import admin
# from .models import User, Transaction

# admin.site.register(User)
# admin.site.register(Transaction)

from django.contrib import admin
from .models import User, Transaction

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'user_name')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('type', 'category', 'amount', 'date', 'description')
