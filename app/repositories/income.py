from database.database import Database
from app.main import config

class IncomeRepository:
    def __init__(self):
        self.db = Database(config["DB_NAME"])

    def create(self, user_id, category_id, amount, currency_id, description=None):
        stmt = self.db.cursor.execute(
            f"""
            INSERT INTO Incomes (user_id, category_id, amount, currency_id, description) VALUES (?,?,?,?,?)
            """,
            (user_id, category_id, amount, currency_id, description)
        )
        self.db.conn.commit()
        return self.db.cursor.lastrowid

    def get_all(self, user_id):
        stmt = self.db.cursor.execute(
            f"""
            SELECT * FROM Incomes WHERE user_id = ?
            """,
            (user_id,)
        ).fetchall()
        return stmt

    def get_by_id(self, user_id, income_id):
        stmt = self.db.cursor.execute(
            f"""
            SELECT * FROM Incomes WHERE user_id = ? AND id = ?
            """,
            (user_id, income_id)
        ).fetchone()
        return stmt

    def delete_by_id(self, user_id, income_id):
        stmt = self.db.cursor.execute(
            f"""
            DELETE FROM Incomes WHERE user_id = ? AND id = ?
            """,
            (user_id, income_id)
        )
        self.db.conn.commit()

    def update_by_id(self, user_id, income_id, category_id, amount, currency_id, description=None):
        stmt = self.db.cursor.execute(
            f"""
            UPDATE Incomes SET category_id = ?, amount = ?, currency_id = ?, description = ? WHERE user_id = ? AND id = ?
            """,
            (category_id, amount, currency_id, description, user_id, income_id)
        )
        self.db.conn.commit()