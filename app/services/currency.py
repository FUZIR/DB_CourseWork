from app.repositories.currency import CurrencyRepository


class CurrencyService:
    def __init__(self):
        self.repository = CurrencyRepository()

    def create(self, currency_name):
        return self.repository.create(currency_name)

    def get_currencies(self):
        return self.repository.get_currencies()

    def get_currency_by_id(self, currency_id):
        return self.repository.get_currency_by_id(currency_id)