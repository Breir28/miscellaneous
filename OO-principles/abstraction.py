from abc import ABC, abstractmethod

class Fahrzeug(ABC):
    @abstractmethod
    def starten(self): # abstarkte Klasse
        pass
    def fahren(self): # normale Klasse
        print("Auto fährt los...")

class Auto(Fahrzeug):
    def starten(self):
        print("Auto startet") 


f = Auto()
f.starten() # Auto startet
f.fahren()  # Auto fährt los...
