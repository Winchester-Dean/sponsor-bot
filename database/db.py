import sqlite3

class DataBase:
    def __init__(self):
        self.directory = "database/database.db"
        self.connect = sqlite3.connect(self.directory)
        self.cursor = self.connect.cursor()

        with self.connect:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER NOT NULL UNIQUE,
                    name TEXT NOT NULL,
                    username TEXT
                )
            """)

        with self.connect:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS admins(
                    id INTEGER PRIMARY KEY,
                    admin_id INTEGER NOT NULL UNIQUE,
                    name TEXT NOT NULL
                )
            """)

        with self.connect:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS channels(
                    id INTEGER PRIMARY KEY,
                    channel_id INTEGER NOT NULL UNIQUE,
                    curl TEXT NOT NULL,
                    name TEXT NOT NULL
                )
            """)

        with self.connect:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS owner(
                    id INTEGER NOT NULL UNIQUE
                )
            """)

    def get_users(self):
        self.cursor.execute(
            "SELECT * FROM users"
        )
        return self.cursor.fetchall()
    
    def get_admins(self):
        self.cursor.execute(
            "SELECT * FROM admins"
        )
        return self.cursor.fetchall()
    
    def get_channels(self):
        self.cusor.execute(
            "SELECT * FROM channels"
        )
        return self.cursor.fetchall()

    def get_users_id(self):
        self.cursor.execute(
            "SELECT user_id FROM users"
        )
        return self.cursor.fetchall()

    def get_admins_id(self):
        self.cursor.execute(
            "SELECT admin_id FROM admins"
        )
        return self.cursor.fetchall()
    
    def get_channels_id(self):
        self.cursor.execute(
            "SELECT channel_id FROM channels"
        )
        return self.cursor.fetchall()

    def get_owners_id(self):
        self.cursor.execute(
            "SELECT id FROM owner"
        )
        return self.cursor.fetchall()
    
    def new_user(
        self,
        user_id: int,
        name: str,
        username: str = None
    ):
        with self.connect:
            self.cursor.execute(
                """INSERT INTO users(
                    user_id, name, username
                ) VALUES (?, ?, ?)""",
                [user_id, name, username]
            )

    def new_admin(
        self,
        admin_id: int,
        name: str
    ):
        with self.connect:
            self.cursor.execute(
                "INSERT INTO admins(admin_id, name) "
                "WHERE (?, ?)",
                [admin_id, name]
            )
    
    def new_channel(
        self,
        channel_id: int,
        curl: str,
        name: str
    ):
        with self.connect:
            self.cursor.execute(
                """INSERT INTO channels(
                    channel_id, curl, name
                ) VALUES (?, ?, ?)""",
                [channel_id, curl, name]
            )

    def del_admin(
        self,
        admin_id: int
    ):
        with self.connect:
            self.cursor.execute(
                "DELETE FROM admins "
                "WHERE admin_id=?",
                [admin_id]
            )

    def del_channel(
        self,
        channel_id: int
    ):
        with self.connect:
            self.cursor.execute(
                "DELETE FROM channels "
                "WHERE channel_id=?",
                [channel_id]
            )

