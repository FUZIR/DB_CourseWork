from database.database import Database
from app.config import DB_NAME

db = Database(DB_NAME)

with open("database/migrations.sql", "r") as f:
    db.cursor.executescript(f.read())

db.close()