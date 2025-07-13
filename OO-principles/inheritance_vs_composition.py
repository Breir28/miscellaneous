# Inheritance
# Eine Klasse erbt von einer anderen – "ist ein"-Beziehung.

class Tier:
    def bewegung(self):
        return "bewegt sich"

class Fisch(Tier):  # Fisch **ist ein** Tier
    def schwimmen(self):
        return "schwimmt"


f = Fisch()
print(f.bewegung())  # bewegt sich
print(f.schwimmen())  # schwimmt



# Composition
# Eine Klasse nutzt eine andere – "hat ein"-Beziehung.

class Flosse:
    def schlagen(self):
        return "Flosse schlägt"

class Fisch:
    def __init__(self):
        self.flosse = Flosse()  # Fisch **hat eine** Flosse

    def schwimmen(self):
        return self.flosse.schlagen() + " → schwimmt"


f = Fisch()
print(f.schwimmen())  # Flosse schlägt → schwimmt
