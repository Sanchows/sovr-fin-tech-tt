from apps.common.repositories import BaseModelRepository


class BaseModelService:
    def __init__(self, repository: BaseModelRepository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, item_id):
        return self.repository.get_by_id(item_id)

    def add(self, **kwargs):
        return self.repository.add(**kwargs)

    def bulk_add(self, items):
        return self.repository.bulk_add(items)

    def update(self, item):
        return self.repository.update(item)

    def delete(self, item_id):
        return self.repository.delete(item_id)
