# =================
# Singleton Pattern
# =================

# Zweck: Sicherstellen, dass eine Klasse nur eine Instanz hat und einen globalen Zugriffspunkt auf diese Instanz bietet.
# Verwendung: Nützlich für Objekte, die global zugänglich sein müssen, wie z.B. Konfigurationsmanager oder Logging-Klassen.

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            # Wenn keine Instanz existiert, wird eine neue Instanz mit Hilfe der __new__-Methode der Superklasse (in diesem Fall object, die Standard-Superklasse in Python) erstellt.
            # super(Singleton, cls).__new__(cls) ruft die __new__-Methode der Superklasse auf, um eine neue Instanz zu erstellen.
            #Diese neue Instanz wird dann der Klassenvariable _instance zugewiesen.
            cls._instance = super(Singleton, cls).__new__(cls)
            # Hier wird ein Attribut value für die neu erstellte Instanz initialisiert und auf None gesetzt. Dies ist ein Beispiel für die Initialisierung eines Instanzattributs.
            cls._instance.value = None 
        return cls._instance

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

# Verwendung des Singletons
singleton1 = Singleton()
singleton1.set_value("Hello, Singleton!")

singleton2 = Singleton()
print(singleton2.get_value())  # Ausgabe: Hello, Singleton!

# Überprüfen, ob beide Instanzen dieselbe sind
print(singleton1 is singleton2)  # Ausgabe: True
