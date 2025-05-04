from app.repositories.income import IncomeRepository


class IncomeService:
    def __init__(self):
        self.repository = IncomeRepository()

    def create(self, user_id, category_id, amount, currency_id, description=None):
        return self.repository.create(user_id, category_id, amount, currency_id, description)

    def get_all(self, user_id):
        return self.repository.get_all(user_id)

    def get_by_id(self, user_id, income_id):
        return self.repository.get_by_id(user_id, income_id)

    def delete_by_id(self, user_id, income_id):
        return self.repository.delete_by_id(user_id, income_id)

    def update_by_id(self, user_id, income_id, category_id, amount, currency_id, description=None):
        return self.repository.update_by_id(user_id, income_id, category_id, amount, currency_id, description)