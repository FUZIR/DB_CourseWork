import bcrypt

from app.main import config
from app.repositories.user import UserRepository


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def register(self, login: str, password: str, name:str, surname:str):
        hashed_password = bcrypt.hashpw(password.encode(), config["SALT"]).decode("utf-8")
        return self.repository.register(login, password, name, surname)

    def login(self, login: str, password: str):
        return self.repository.login(login, password)