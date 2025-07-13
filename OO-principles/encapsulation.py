class Konto:
    def __init__(self):
        self.__saldo = 0  # private

    def einzahlen(self, betrag): # public
        if betrag > 0:
            self.__saldo += betrag
            return True
        return False

    def auszahlen(self, betrag): # public
        if betrag <= self.__saldo:
            self.__saldo -= betrag
            return True
        return False

    def saldo_anzeigen(self): # public
        return self.__saldo


k = Konto()
k.einzahlen(100)
k.auszahlen(25)
print("Saldo:", k.saldo_anzeigen())  # Saldo: 100
