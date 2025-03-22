from django.db import models
from django.utils.translation import gettext as _

from apps.common.models import CreatedAtModel


class Manufacturer(CreatedAtModel):
    name = models.CharField(verbose_name=_("Название производителя"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Производитель")
        verbose_name_plural = _("Производители")


class Product(CreatedAtModel):
    name = models.CharField(verbose_name=_("Название товара"), max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        Product.objects.create()
        return self.name

    class Meta:
        verbose_name = _("Товар")
        verbose_name_plural = _("Товары")


class Contract(CreatedAtModel):
    details = models.TextField(verbose_name=_("Детали контракта"))

    def __str__(self):
        return f"Контракт №{self.pk}"

    class Meta:
        verbose_name = _("Контракт")
        verbose_name_plural = _("Контракты")


class CreditApplication(CreatedAtModel):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name="credit_application")
    products = models.ManyToManyField(Product, through="CreditApplicationProduct", related_name="credit_applications")

    def __str__(self):
        return f"Кредитная заявка №{self.pk}"

    class Meta:
        verbose_name = _("Кредитная заявка")
        verbose_name_plural = _("Кредитные заявки")


class CreditApplicationProduct(CreatedAtModel):
    credit_application = models.ForeignKey(CreditApplication, on_delete=models.CASCADE,
                                           related_name="applications_products")

    # по ТЗ - "товар может принадлежать только одной кредитной заявке", поэтому OneToOneField
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="applications_products")

    def __str__(self):
        return f"Связь: {self.credit_application} и {self.product}"

    class Meta:
        verbose_name = _("Связь кредитной заявки с товаром")
        verbose_name_plural = _("Связи кредитных заявок с товарами")

        unique_together = ("credit_application", "product")
