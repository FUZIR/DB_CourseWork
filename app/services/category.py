from app.repositories.category import CategoryRepository


class CategoryService:
    def __init__(self):
        self.repository = CategoryRepository()

    def create(self, category_name):
        return self.repository.create(category_name)

    def get_all(self):
        return self.repository.get_all()
