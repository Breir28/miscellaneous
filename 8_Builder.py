# ===============
# Builder Pattern
# ===============

# Zweck: Trennt die Konstruktion eines komplexen Objekts von seiner Darstellung, so dass derselbe Konstruktionsprozess verschiedene Darstellungen erstellen kann.
# Verwendung: Nützlich, wenn ein Objekt in mehreren Schritten erstellt werden muss.

from abc import ABC, abstractmethod

# Produkt
class Pizza:
    def __init__(self):
        self.dough = ""
        self.sauce = ""
        self.topping = ""

    def __str__(self):
        return f"Pizza with {self.dough} dough, {self.sauce} sauce, and {self.topping} topping."

# Builder Interface
class PizzaBuilder(ABC):
    @abstractmethod
    def set_dough(self):
        pass

    @abstractmethod
    def set_sauce(self):
        pass

    @abstractmethod
    def set_topping(self):
        pass

    @abstractmethod
    def get_pizza(self) -> Pizza:
        pass

# Konkreter Builder
class HawaiianPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def set_dough(self):
        self.pizza.dough = "cross"

    def set_sauce(self):
        self.pizza.sauce = "mild"

    def set_topping(self):
        self.pizza.topping = "ham and pineapple"

    def get_pizza(self) -> Pizza:
        return self.pizza

class SpicyPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def set_dough(self):
        self.pizza.dough = "pan baked"

    def set_sauce(self):
        self.pizza.sauce = "hot"

    def set_topping(self):
        self.pizza.topping = "pepperoni and salami"

    def get_pizza(self) -> Pizza:
        return self.pizza

# Director
class Cook:
    def __init__(self, pizza_builder: PizzaBuilder):
        self.pizza_builder = pizza_builder

    def make_pizza(self):
        self.pizza_builder.set_dough()
        self.pizza_builder.set_sauce()
        self.pizza_builder.set_topping()

    def get_pizza(self) -> Pizza:
        return self.pizza_builder.get_pizza()

# Verwendung
hawaiian_builder = HawaiianPizzaBuilder()
cook = Cook(hawaiian_builder)
cook.make_pizza()
hawaiian_pizza = cook.get_pizza()
print(hawaiian_pizza)

spicy_builder = SpicyPizzaBuilder()
cook = Cook(spicy_builder)
cook.make_pizza()
spicy_pizza = cook.get_pizza()
print(spicy_pizza)
