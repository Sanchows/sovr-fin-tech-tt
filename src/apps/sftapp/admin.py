from django.contrib import admin

from apps.sftapp.models import Manufacturer, Product, Contract, CreditApplication, CreditApplicationProduct


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    pass


class ApplicationProductInline(admin.TabularInline):
    model = CreditApplicationProduct
    extra = 1

@admin.register(CreditApplication)
class CreditApplicationAdmin(admin.ModelAdmin):
    inlines = [ApplicationProductInline]
