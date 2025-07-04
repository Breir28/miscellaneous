# ================
# Strategy Pattern
# ================

# Zweck: Definiert eine Familie von Algorithmen, kapselt jeden einzelnen und macht sie austauschbar. Der Algorithmus kann zur Laufzeit ausgewählt werden.
# Verwendung: Nützlich, wenn verschiedene Varianten eines Algorithmus benötigt werden und zwischen ihnen umgeschaltet werden soll.

from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Paying {amount} using Credit Card {self.card_number}.")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paying {amount} using PayPal account {self.email}.")

class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        print(f"Paying {amount} using Crypto wallet {self.wallet_address}.")

# Context
class PaymentContext:
    def __init__(self, payment_strategy: PaymentStrategy):
        self._payment_strategy = payment_strategy

    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        self._payment_strategy = payment_strategy

    def execute_payment(self, amount):
        self._payment_strategy.pay(amount)

# Usage
credit_card_payment = CreditCardPayment("1234-5678-9012-3456")
paypal_payment = PayPalPayment("user@example.com")
crypto_payment = CryptoPayment("1A2b3C4d5E6f7G8h9I0j")

payment_context = PaymentContext(credit_card_payment)
payment_context.execute_payment(100)

payment_context.set_payment_strategy(paypal_payment)
payment_context.execute_payment(50)

payment_context.set_payment_strategy(crypto_payment)
payment_context.execute_payment(200)
