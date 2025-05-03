from database.database import Database
from app.main import config
import bcrypt


class User:
    def __init__(self):
        self.db = Database(config["DB_NAME"])

    def register(self, login: str, password: str, name:str, surname:str):
        stmt =  self.db.cursor.execute(
            f"""
            INSERT INTO USERS (login, password, name, surname) VALUES (?,?,?,?)
            """,
            (login, bcrypt.hashpw(password.encode(), config["SALT"]).decode("utf-8"), name, surname)
        )
        self.db.conn.commit()
        return self.db.cursor.lastrowid

    def login(self, login: str, password: str):
        stmt = self.db.cursor.execute(
            "SELECT * FROM USERS WHERE login = ?",
            (login,)
        )
        user = stmt.fetchone()
        if user is None:
            return None

        hashed_password = user[4]
        if bcrypt.checkpw(password.encode(), hashed_password.encode()):
            return user
        return None