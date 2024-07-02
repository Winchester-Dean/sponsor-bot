import sqlite3

connect = sqlite3.connect("database/database.db")
cursor = connect.cursor()

with connect:
    cursor.execute(
        "INSERT INTO owner VALUES (?)",
        [6099758454]
    )
