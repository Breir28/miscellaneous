# ==================
# Decorator Pattern
# ==================

# Zweck: Fügt einem Objekt dynamisch neue Verantwortlichkeiten hinzu, ohne seine Klasse zu ändern.
# Verwendung: Nützlich, um Funktionalität zu erweitern, ohne Unterklassen zu erstellen.

from abc import ABC, abstractmethod

# Komponente
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

# Konkrete Komponente
class SimpleCoffee(Coffee):
    def cost(self):
        return 5

# Abstrakter Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Konkrete Decoratoren
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

# Verwendung
coffee = SimpleCoffee()
print(f"Cost of simple coffee: {coffee.cost()}")

coffee_with_milk = MilkDecorator(coffee)
print(f"Cost of coffee with milk: {coffee_with_milk.cost()}")

coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
print(f"Cost of coffee with milk and sugar: {coffee_with_milk_and_sugar.cost()}")
