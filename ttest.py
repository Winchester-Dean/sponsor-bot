import sqlite3

connect = sqlite3.connect("database/database.db")
cursor = connect.cursor()

with connect:
    cursor.execute(
        "DELETE FROM `channels` WHERE `id`='5';"
    )
