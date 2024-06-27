import sqlite3

class DataBase:
    def __init__(self):
        self.directory: str = "database/database.db"
        self.connect = sqlite3.connect(self.directory)
        self.cursor = self.connect.cursor()

        with self.connect:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER NOT NULL UNIQUE,
                    name TEXT NOT NULL
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
                    chid INTEGER NOT NULL,
                    curl TEXT NOT NULL,
                    name TEXT NOT NULL
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
        self.cursor.execute(
            "SELECT * FROM channels"
        )
        return self.cursor.fetchall()
    
    def get_channels_id(self):
        self.cursor.execute(
            "SELECT chid FROM channels"
        )
        return self.cursor.fetchall()
    
    def get_admins_id(self):
        self.cursor.execute(
            "SELECT admin_id FROM admins"
        )
        return self.cursor.fetchall()
    
    def get_users_id(self):
        self.cursor.execute(
            "SELECT user_id FROM users"
        )
        return self.cursor.fetchall()
    
    def add_new_user(
        self,
        user_id: int,
        name: str
    ):
        if user_id and name:
            with self.connect:
                self.cursor.execute(
                    "INSERT INTO users(user_id, name) "
                    "VALUES (?, ?)",
                    [user_id, name]
                )
    
    def add_new_admin(
        self,
        admin_id: int,
        name: str
    ):
        if admin_id and name:
            with self.connect:
                self.cursor.execute(
                    "INSERT INTO admins(admin_id, name) "
                    "VALUES (?, ?)",
                    [admin_id, name]
                )
    
    def add_new_channel(
        self,
        chid: int,
        curl: str,
        name: str
    ):
        if chid and curl and name:
            with self.connect:
                self.cursor.execute(
                    "INSERT INTO channels(chid, curl, name) "
                    "VALUES (?, ?, ?)",
                    [chid, curl, name]
                )
