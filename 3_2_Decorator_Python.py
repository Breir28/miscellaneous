# ==================
# Decorator Pattern
# ==================

# Komponente
def simple_coffee():
    return 5

# Decorator-Funktionen
def milk_decorator(coffee_func):
    def wrapper():
        cost = coffee_func() + 2
        print("Adding milk")
        return cost
    return wrapper

def sugar_decorator(coffee_func):
    def wrapper():
        cost = coffee_func() + 1
        print("Adding sugar")
        return cost
    return wrapper

# Verwendung der Decoratoren mit @-Syntax
@sugar_decorator
@milk_decorator
def my_coffee():
    return simple_coffee()

# Testen der Decoratoren
print(f"Cost of my coffee: {my_coffee()}")


# so funktioniert es eigentlich
# print(sugar_decorator(milk_decorator(my_coffee))())