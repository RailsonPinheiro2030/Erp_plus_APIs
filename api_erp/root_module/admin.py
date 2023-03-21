
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users, Company, Module, Storage, RiskClass
from django.contrib.auth.models import Group
from stock_module.models import Stock



class CustomGroup(Group):
    class Meta:
        proxy = True
        verbose_name = 'Grupo personalizado'
        verbose_name_plural = 'Grupos personalizados'


class CustomUserAdmin(UserAdmin):
    model = Users
    # list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'company')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'company', 'modules', 'is_admin')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','last_name', 'username','email', 'password1', 'password2', 'company', 'modules', 'is_admin'),
        }),
)

class StorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'company')
    autocomplete_fields = []



admin.site.unregister(Group)
admin.site.register(CustomGroup)
admin.site.register(Users, CustomUserAdmin)
admin.site.register(Company)
admin.site.register(Module)
admin.site.register(RiskClass)
admin.site.register(Stock)
admin.site.register(Storage, StorageAdmin)
