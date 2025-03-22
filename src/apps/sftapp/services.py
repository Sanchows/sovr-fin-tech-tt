from apps.common.services import BaseModelService
from apps.sftapp.repositories import CreditApplicationRepository, ProductRepository, ManufacturerRepository, \
    ContractRepository


class ProductService(BaseModelService):
    def __init__(self):
        super().__init__(repository=ProductRepository())


class ManufacturerService(BaseModelService):
    def __init__(self):
        super().__init__(repository=ManufacturerRepository())


class ContractService(BaseModelService):
    def __init__(self):
        super().__init__(repository=ContractRepository())


class CreditApplicationService(BaseModelService):
    def __init__(self):
        super().__init__(repository=CreditApplicationRepository())

    def get_unique_manufacturer_ids_by_contract_id(self, contract_id):
        unique_manufacturer_ids = self.repository.model.objects \
            .filter(contract_id=contract_id) \
            .distinct('products__manufacturer_id') \
            .values_list('products__manufacturer_id', flat=True)

        # Когда запрос не нашел ни одного manufacturer_id - возвращает QuerySet с одним элементом None.
        if unique_manufacturer_ids and unique_manufacturer_ids[0] is None:
            return set()
        return set(unique_manufacturer_ids)

    @staticmethod
    def set_products(instance, products):
        return instance.products.set(products)
