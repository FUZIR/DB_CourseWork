from database.database import Database

class Outcome:
    def __init__(self):
        self.db = Database(config["DB_NAME"])

    def create(self, user_id, category_id, amount, currency_id, date, description):
        stmt = self.db.cursor.execute(
            f"""
            INSERT INTO Outcomes (user_id, category_id, amount, currency_id, date, description) VALUES (?,?,?,?,?,?)
            """,
            (user_id, category_id, amount, currency_id, date, description)
        )
        self.db.conn.commit()
        return self.db.cursor.lastrowid

    def get_all(self, user_id):
        stmt = self.db.cursor.execute(
            f"""
            SELECT * FROM Outcomes WHERE user_id = ?
            """,
            (user_id,)
        ).fetchall()
        return stmt

    def get_by_id(self, user_id, outcome_id):
        stmt = self.db.cursor.execute(
            f"""
            SELECT * FROM Outcomes WHERE user_id = ? AND id = ?
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

    def update_by_id(self, user_id, outcome_id, category_id, amount, currency_id, date, description):
        stmt = self.db.cursor.execute(
            f"""
            UPDATE Outcomes SET category_id = ?, amount = ?, currency_id = ?, date = ?, description = ? WHERE user_id = ? AND id = ?
            """,
            (category_id, amount, currency_id, date, description, user_id, outcome_id)
        )
        self.db.conn.commit()
