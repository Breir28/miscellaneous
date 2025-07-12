# ===============
# Factory Pattern
# ===============

# Zweck: Definiert eine Schnittstelle zur Erstellung von Objekten, wobei die konkrete Klasse der zu erstellenden Objekte von Unterklassen entschieden wird.
# Verwendung: Nützlich, wenn eine Methode verschiedene Arten von Objekten erstellen muss und die konkrete Klasse der Objekte nicht im Voraus bekannt ist.

from abc import ABC, abstractmethod

# Abstraktes Tier
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Konkrete Tiere
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Fabrik
class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")

# Verwendung der Fabrik
factory = AnimalFactory()

dog = factory.create_animal("dog")
print(dog.speak())  # Ausgabe: Woof!

cat = factory.create_animal("cat")
print(cat.speak())  # Ausgabe: Meow!
