# ==========================
# Data Access Object Pattern
# ==========================

import sqlite3
from sqlite3 import Error

# Benutzerklasse, die die Datenstruktur darstellt
class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

# DAO für Benutzer mit SQLite
class UserDAO:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None
        self._connect()

    def _connect(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            self._create_table()
        except Error as e:
            print(e)

    def _create_table(self):
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            self.connection.commit()
        except Error as e:
            print(e)

    def add_user(self, user):
        sql = ''' INSERT INTO users(user_id, username, email)
                  VALUES(?,?,?) '''
        cursor = self.connection.cursor()
        cursor.execute(sql, (user.user_id, user.username, user.email))
        self.connection.commit()

    def get_user(self, user_id):
        sql = "SELECT * FROM users WHERE user_id=?"
        cursor = self.connection.cursor()
        cursor.execute(sql, (user_id,))
        row = cursor.fetchone()
        if row:
            return User(row[0], row[1], row[2])
        return None

    def update_user(self, user):
        sql = ''' UPDATE users
                  SET username = ?,
                      email = ?
                  WHERE user_id = ?'''
        cursor = self.connection.cursor()
        cursor.execute(sql, (user.username, user.email, user.user_id))
        self.connection.commit()
        return cursor.rowcount > 0

    def delete_user(self, user_id):
        sql = 'DELETE FROM users WHERE user_id=?'
        cursor = self.connection.cursor()
        cursor.execute(sql, (user_id,))
        self.connection.commit()
        return cursor.rowcount > 0

    def __del__(self):
        if self.connection:
            self.connection.close()

# Beispiel für die Verwendung des DAO
user_dao = UserDAO('Design Patterns/users.db')

# Einen neuen Benutzer hinzufügen
new_user = User(1, "johndoe", "john@example.com")
user_dao.add_user(new_user)

# Einen Benutzer abrufen
user = user_dao.get_user(1)
print(f"User found: {user.username}, {user.email}")

# Einen Benutzer aktualisieren
updated_user = User(1, "johndoeupdated", "john.updated@example.com")
user_dao.update_user(updated_user)
print(f"Updated user: {user_dao.get_user(1).username}, {user_dao.get_user(1).email}")

# Einen Benutzer löschen
user_dao.delete_user(1)
print(f"User with id 1 exists after deletion: {user_dao.get_user(1) is not None}")
