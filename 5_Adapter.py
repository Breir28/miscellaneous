# ===============
# Adapter Pattern
# ===============

# Zweck: Wandelt die Schnittstelle einer Klasse in eine andere Schnittstelle um, die die Clients erwarten. Lässt Klassen zusammenarbeiten, die sonst nicht zusammenarbeiten könnten.
# Verwendung: Nützlich, um inkompatible Schnittstellen zu integrieren.

# Zielschnittstelle, die der Client erwartet
class EuropeanSocketInterface:
    def voltage(self):
        pass

    def live(self):
        pass

    def neutral(self):
        pass

    def earth(self):
        pass

# Ein konkretes Objekt, das der Client verwenden möchte
class AmericanSocket:
    def voltage(self):
        return 120

    def live(self):
        return 1

    def neutral(self):
        return -1

# Adapter, der die inkompatible Schnittstelle anpasst
class Adapter(EuropeanSocketInterface):
    def __init__(self, american_socket):
        self.american_socket = american_socket

    def voltage(self):
        # Konvertierung der Spannung von 120V auf 230V
        return 230

    def live(self):
        return self.american_socket.live()

    def neutral(self):
        return self.american_socket.neutral()

    def earth(self):
        # Amerikanische Steckdosen haben oft keine Erde, daher geben wir 0 zurück
        return 0

# Client-Code, der die europäische Steckdose erwartet
class ElectricKettle:
    def __init__(self, socket: EuropeanSocketInterface):
        self.socket = socket

    def boil(self):
        if self.socket.voltage() > 200:
            print("Kettle is boiling.")
        else:
            print("Not enough voltage to boil the kettle.")

# Verwendung
american_socket = AmericanSocket()

kettle = ElectricKettle(american_socket)
kettle.boil()

adapter = Adapter(american_socket)

kettle = ElectricKettle(adapter)
kettle.boil()
