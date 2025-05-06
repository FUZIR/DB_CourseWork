from database.database import Database
from app.config import DB_NAME

class IncomeRepository:
    def __init__(self):
        self.db = Database(DB_NAME)

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
            f"""SELECT Incomes.id, Incomes.user_id, Incomes.category_id, Incomes.amount, Incomes.currency_id, Currencies.currency_name, 
                           Incomes.date, Incomes.description, Categories.category_name
                    FROM Incomes
                    JOIN Categories ON Incomes.category_id = Categories.id
                    JOIN Currencies ON Incomes.currency_id = Currencies.id
                    WHERE Incomes.user_id = ?
                    """,
            (user_id,)
        ).fetchall()
        return stmt

    def get_by_id(self, user_id, income_id):
        stmt = self.db.cursor.execute(
            f"""
                    SELECT Incomes.id, Incomes.user_id, Incomes.category_id, Incomes.currency_id, Currencies.currency_name, 
                           Incomes.date, Incomes.description, Categories.category_name
                    FROM Incomes
                    JOIN Categories ON Incomes.category_id = Categories.id
                    JOIN Currencies ON Incomes.currency_id = Currencies.id
                    WHERE Incomes.user_id = ? AND Incomes.id = ?
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