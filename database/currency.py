from database.database import Database
from app.main import config

class Currency:
    def __init__(self):
        self.db = Database(config["DB_NAME"])

    def create(self, currency_name):
        stmt = self.db.cursor.execute(
            f"""
            INSERT INTO CURRENCIES (currency_name) VALUES (?)
            """,
            (currency_name,)
        )
        self.db.conn.commit()
        return self.db.cursor.lastrowid

    def get_currencies(self):
        stmt = self.db.cursor.execute(
            """
            SELECT * FROM Currencies
            """
        ).fetchall()
        return stmt

    def get_currency_by_id(self, currency_id):
        stmt = self.db.cursor.execute(
            "SELECT * FROM Currencies WHERE currency_id = ?",
            (currency_id,)
        )
        return stmt.fetchone()