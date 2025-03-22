from django.db import models
from django.utils.translation import gettext as _


class CreatedAtModel(models.Model):
    created_at = models.DateTimeField(verbose_name=_("Дата создания записи"), auto_now_add=True)

    class Meta:
        abstract = True
