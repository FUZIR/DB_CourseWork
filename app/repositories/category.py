from database.database import Database
from app.config import DB_NAME

class CategoryRepository:
    def __init__(self):
        self.db = Database(DB_NAME)

    def create(self, category_name):
        stmt = self.db.cursor.execute(
            f"""
            INSERT INTO CATEGORIES (category_name) VALUES (?)
            """,
            (category_name,)
        )
        self.db.conn.commit()
        return self.db.cursor.lastrowid

    def get_all(self):
        stmt = self.db.cursor.execute(
            """
            SELECT * FROM Categories
            """
        ).fetchall()
        return stmt

