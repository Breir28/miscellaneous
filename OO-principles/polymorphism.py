class Tier:
    def sprich(self):
        return "Laut"

class Hund(Tier):
    def sprich(self):
        return "Wuff"

class Katze(Tier):
    def sprich(self):
        return "Miau"

def tier_spricht(tier):
    print(tier.sprich())

# Ausführung
tier_spricht(Tier())   # Laut
tier_spricht(Hund())   # Wuff
tier_spricht(Katze())  # Miau
