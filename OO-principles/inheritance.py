class Tier:
    def sprich(self):
        return "Laut"

class Hund(Tier):
    def sprich(self):
        return "Wuff"
    
class Katze(Tier):
    def sprich(self):
        return "Miau"    

# Ausführung
t = Tier()
h = Hund()
k = Katze()
print("Tier:", t.sprich())  # Tier: Laut
print("Hund:", h.sprich())  # Hund: Wuff
print("Katze:", k.sprich())  # Katze: Miau
