# ==========================
# Data Access Object Pattern
# ==========================

# Zweck: Abstrahiert und kapselt den Zugriff auf eine Datenquelle, um die Datenzugriffslogik von der Geschäftslogik zu trennen.
# Verwendung: Nützlich für Datenbankoperationen, um die Komplexität des Datenzugriffs zu verbergen und die Wartbarkeit zu verbessern.

# Benutzerklasse, die die Datenstruktur darstellt
class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

# DAO für Benutzer
class UserDAO:
    def __init__(self):
        # In einer echten Anwendung wäre dies eine Datenbankverbindung
        self.users = {}

    def add_user(self, user):
        self.users[user.user_id] = user

    def get_user(self, user_id):
        return self.users.get(user_id)

    def update_user(self, user):
        if user.user_id in self.users:
            self.users[user.user_id] = user
            return True
        return False

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

# Beispiel für die Verwendung des DAO
user_dao = UserDAO()

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
