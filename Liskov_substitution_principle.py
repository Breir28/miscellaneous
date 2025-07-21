# Liskov Substitution Principle (LSP)
# Instanzen einer Basisklasse müssen durch Instanzen ihrer Subklassen ersetzbar sein.

# Schlechtes Beispiel:
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies")

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostrich can't fly")
    
# Refactord
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        pass

class Sparrow(FlyingBird):
    def fly(self):
        print("Sparrow flies")

class Ostrich(Bird):
    pass

