from app.repositories.outcome import OutcomeRepository


class OutcomeService:
    def __init__(self):
        self.repository = OutcomeRepository()

    def create(self, user_id, category_id, amount, currency_id, date, description):
        return self.repository.create(user_id, category_id, amount, currency_id, date, description)

    def get_all(self, user_id):
        return self.repository.get_all(user_id)

    def get_by_id(self, user_id, outcome_id):
        return self.repository.get_by_id(user_id, outcome_id)

    def delete_by_id(self, user_id, outcome_id):
        return self.repository.delete_by_id(user_id, outcome_id)

    def update_by_id(self, user_id, outcome_id, category_id, amount, currency_id, date, description):
        return self.repository.update_by_id(user_id, outcome_id, category_id, amount, currency_id, date, description)