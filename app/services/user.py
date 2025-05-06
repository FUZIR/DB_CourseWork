import bcrypt

from app.repositories.user import UserRepository


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def register(self, login: str, password: str, name:str, surname:str):
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode("utf-8")
        user_id = self.repository.register(login, hashed_password, name, surname)
        return user_id

    def login(self, login: str, password: str):
        user = self.repository.login(login, password)
        return user