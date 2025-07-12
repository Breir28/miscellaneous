# ================
# Observer Pattern
# ================

# Zweck: Definiert eine Eins-zu-Viele-Abhängigkeit zwischen Objekten, so dass, wenn sich der Zustand eines Objekts ändert, alle abhängigen Objekte benachrichtigt und automatisch aktualisiert werden.
# Verwendung: Wird oft in Event-Handling-Systemen verwendet.

from abc import ABC, abstractmethod

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

# Concrete Observer
class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'{self.name} received message: {message}')

# Subject (Observable)
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

# Usage
subject = Subject()

observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

subject.attach(observer1)
subject.attach(observer2)

subject.notify("Hello Observers!")

subject.detach(observer1)

subject.notify("Hello Observer 2!")
