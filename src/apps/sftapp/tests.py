from django.test import TestCase

from apps.sftapp.services import CreditApplicationService, ProductService, ManufacturerService, ContractService


class UniqueManufacturerFromCreditApplicationsTestCase(TestCase):
    def setUp(self):
        self.contract_service = ContractService()
        self.manufacturer_service = ManufacturerService()
        self.product_service = ProductService()
        self.credit_application_service = CreditApplicationService()

        # Создание контрактов
        self.contract_first = self.contract_service.add(details='lorem ipsum.')
        self.contract_second = self.contract_service.add(details='big lorem ipsum.')
        self.contract_third = self.contract_service.add(details='veeery big lorem ipsum.')

        # Создание производителей
        self.manufacturer_first = self.manufacturer_service.add(name="OOO the One")
        self.manufacturer_second = self.manufacturer_service.add(name="OOO the Two")
        self.manufacturer_third = self.manufacturer_service.add(name="OOO the Third")
        self.manufacturer_fourth = self.manufacturer_service.add(name="OOO the Fourth")

        # Создание товаров
        products_part_one = self.product_service.bulk_add((
                dict(name="p1", manufacturer=self.manufacturer_first),
                dict(name="p2", manufacturer=self.manufacturer_first),
                dict(name="p3", manufacturer=self.manufacturer_first),
            )
        )
        products_part_two = self.product_service.bulk_add((
                dict(name="p11", manufacturer=self.manufacturer_first),
                dict(name="my 11", manufacturer=self.manufacturer_second),
                dict(name="my 22", manufacturer=self.manufacturer_second),
                dict(name="my 33", manufacturer=self.manufacturer_second),
                dict(name="my 1235", manufacturer=self.manufacturer_fourth),
                dict(name="my 1233", manufacturer=self.manufacturer_fourth),
                dict(name="my 423", manufacturer=self.manufacturer_fourth),
                dict(name="my 12341", manufacturer=self.manufacturer_fourth),
            )
        )

        # Создание кредитных заявок
        self.credit_application_service.get_all()
        # кредитная заявка, в которой 1 уникальный производитель
        credit_application_one = self.credit_application_service.add(contract=self.contract_first)
        self.credit_application_service.set_products(credit_application_one, products_part_one)

        # кредитная заявка, в которой множество уникальных производителей
        credit_application_two = self.credit_application_service.add(contract=self.contract_second)
        self.credit_application_service.set_products(credit_application_two, products_part_two)

        # кредитная заявка, в которой 0 уникальных производителей
        self.credit_application_service.add(contract=self.contract_third)

    def test_contract_with_one_unique_manufacture(self):
        result = self.credit_application_service.get_unique_manufacturer_ids_by_contract_id(self.contract_first.id)

        expected_ids = {self.manufacturer_first.id}
        self.assertSetEqual(result, expected_ids)

    def test_contract_with_many_unique_manufacture(self):
        result = self.credit_application_service.get_unique_manufacturer_ids_by_contract_id(self.contract_second.id)

        expected_ids = {self.manufacturer_first.id, self.manufacturer_fourth.id, self.manufacturer_second.id}
        self.assertSetEqual(result, expected_ids)

    def test_contract_with_no_unique_manufacture(self):
        result = self.credit_application_service.get_unique_manufacturer_ids_by_contract_id(self.contract_third.id)

        expected_ids = set()
        self.assertSetEqual(result, expected_ids)
