from apps.common.repositories import BaseModelRepository
from apps.sftapp.models import Product, Manufacturer, Contract, CreditApplication


class ProductRepository(BaseModelRepository):
    model = Product


class ManufacturerRepository(BaseModelRepository):
    model = Manufacturer


class ContractRepository(BaseModelRepository):
    model = Contract


class CreditApplicationRepository(BaseModelRepository):
    model = CreditApplication
