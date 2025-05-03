from database.database import Database
from app.main import config

db = Database(config["DB_NAME"])

with open("database/migrations.sql", "r") as f:
    db.cursor.executescript(f.read())