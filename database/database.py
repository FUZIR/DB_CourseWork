import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(f"../{db_name}")
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()