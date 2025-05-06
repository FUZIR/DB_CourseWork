import bcrypt

from database.database import Database
from app.config import DB_NAME


class UserRepository:
    def __init__(self):
        self.db = Database(DB_NAME)

    def register(self, login: str, password: str, name:str, surname:str):
        stmt = self.db.cursor.execute(
            "SELECT * FROM Users WHERE login = ?",
            (login,)
        )
        user = stmt.fetchone()
        if user:
            return None

        stmt = self.db.cursor.execute(
            f"""
                    INSERT INTO Users (login, password, name, surname) VALUES (?,?,?,?)
                    """,
            (login, password, name, surname)
        )
        self.db.conn.commit()
        return self.db.cursor.lastrowid

    def login(self, login: str, password: str):
        stmt = self.db.cursor.execute(
            "SELECT * FROM Users WHERE login = ?",
            (login,)
        )
        user = stmt.fetchone()
        if user is None:
            return None

        hashed_password = user[4]
        if bcrypt.checkpw(password.encode(), hashed_password.encode()):
            return user
        return None