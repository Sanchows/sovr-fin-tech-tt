from typing import Type

from django.db.models import Model


class BaseModelRepository:
    model: Type[Model]

    def get_all(self):
        return self.model.objects.all()

    def get_by_id(self, item_id):
        return self.model.objects.get(id=item_id)

    def add(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def bulk_add(self, items):
        return self.model.objects.bulk_create(self.model(**item) for item in items)

    def update(self, item):
        return item.save()

    def delete(self, item_id):
        item = self.get_by_id(item_id)
        item.delete()
