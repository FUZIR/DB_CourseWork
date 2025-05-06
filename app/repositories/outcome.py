from database.database import Database
from app.config import DB_NAME

class OutcomeRepository:
    def __init__(self):
        self.db = Database(DB_NAME)

    def create(self, user_id, category_id, amount, currency_id, date, purpose):
        stmt = self.db.cursor.execute(
            f"""
            INSERT INTO Outcomes (user_id, category_id, amount, currency_id, date, purpose) VALUES (?,?,?,?,?,?)
            """,
            (user_id, category_id, amount, currency_id, date, purpose)
        )
        self.db.conn.commit()
        return self.db.cursor.lastrowid

    def get_all(self, user_id):
        stmt = self.db.cursor.execute(
            f"""SELECT Outcomes.id, Outcomes.user_id, Outcomes.category_id, Outcomes.amount, Outcomes.currency_id, Currencies.currency_name,
                           Outcomes.date, Outcomes.purpose, Categories.category_name
                    FROM Outcomes
                    JOIN Categories ON Outcomes.category_id = Categories.id
                    JOIN Currencies ON Outcomes.currency_id = Currencies.id
                    WHERE Outcomes.user_id = ?
                    """,
            (user_id,)
        ).fetchall()
        return stmt

    def get_by_id(self, user_id, outcome_id):
        stmt = self.db.cursor.execute(
            f"""
                                SELECT Outcomes.id, Outcomes.user_id, Outcomes.category_id, Outcomes.amount, Outcomes.currency_id, Currencies.currency_name,
                                       Outcomes.date, Outcomes.purpose, Categories.category_name
                                FROM Outcomes
                                JOIN Categories ON Outcomes.category_id = Categories.id
                                JOIN Currencies ON Outcomes.currency_id = Currencies.id
                                WHERE Outcomes.user_id = ? AND Outcomes.id = ?
                                """,
            (user_id, outcome_id)
        ).fetchone()
        return stmt

    def delete_by_id(self, user_id, outcome_id):
        stmt = self.db.cursor.execute(
            f"""
            DELETE FROM Outcomes WHERE user_id = ? AND id = ?
            """,
            (user_id, outcome_id)
        )
        self.db.conn.commit()

    def update_by_id(self, user_id, outcome_id, category_id, amount, currency_id, date, purpose):
        stmt = self.db.cursor.execute(
            f"""
            UPDATE Outcomes SET category_id = ?, amount = ?, currency_id = ?, date = ?, purpose = ? WHERE user_id = ? AND id = ?
            """,
            (category_id, amount, currency_id, date, purpose, user_id, outcome_id)
        )
        self.db.conn.commit()
