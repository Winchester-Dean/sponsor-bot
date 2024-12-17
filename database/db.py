import sqlite3

class DataBase:
    def __init__(
        self,
        directory: str = "database.db"
    ):
        self.connect = sqlite3.connect(directory)
        self.cursor = self.connect.cursor()

        with self.connect:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    name INTEGER NOT NULL
                )
            """)
        
        with self.connect:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS admins(
                    id INTEGER PRIMARY KEY,
                    admin_id INTEGER NOT NULL,
                    name TEXT NOT NULL
                )
            """)

        with self.connect:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS channels(
                    id INTEGER PRIMARY KEY,
                    channel_id INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    link TEXT NOT NULL
                )
            """)
    
    def add_user(
        self,
        user_id: int,
        name: str
    ):
        with self.connect:
            self.cursor.execute(
                "INSERT INTO users(user_id, name) "
                "VALUES(?, ?)",
                [user_id, name]
            )
    
    def add_admin(
        self,
        admin_id: int,
        name: str
    ):
        with self.connect:
            self.cursor.execute(
                "INSERT INTO admins(admin_id, name) "
                "VALUES(?, ?)",
                [admin_id, name]
            )
    
    def add_channel(
        self,
        channel_id: int,
        name: str,
        link: str
    ):
        with self.connect:
            self.cursor.execute(
                "INSERT INTO channels(channel_id, name, link) "
                "VALUES(?, ?, ?)",
                [channel_id, name, link]
            )
    
    def remove_admin(
        self,
        admin_id: int
    ):
        with self.connect:
            self.cursor.execute(
                "DELETE FROM admins "
                "WHERE admin_id=?",
                [admin_id]
            )
    
    def remove_channel(
        self,
        channel_id: int
    ):
        with self.connect:
            self.cursor.execute(
                "DELETE FROM channels "
                "WHERE channel_id=?",
                [channel_id]
            )
    
    def get_users(self):
        self.cursor.execute(
            "SELECT user_id, name FROM users"
        )
        return self.cursor.fetchall()
    
    def get_admins(self):
        self.cursor.execute(
            "SELECT admin_id, name FROM admins"
        )
        return self.cursor.fetchall()
    
    def get_channels(self):
        self.cursor.execute(
            "SELECT channel_id, name, link FROM channels"
        )
        return self.cursor.fetchall()

    def get_user_ids(self):
        self.cursor.execute(
            "SELECT user_id FROM users"
        )
        return [row[0] for row in self.cursor.fetchall()]
    
    def get_admin_ids(self):
        self.cursor.execute(
            "SELECT admin_id FROM admins"
        )
        return [row[0] for row in self.cursor.fetchall()]
    
    def get_channels_id(self):
        self.cursor.execute(
            "SELECT channel_id FROM channels"
        )
        return [row[0] for row in self.cursor.fetchall()]

