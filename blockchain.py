##################################################################################################################################
# BLOCKCHAIN
#
# Schlüsselkonzepte für die Sicherheit einer Blockchain:
# - Hashwert des Vorgängerblocks ist eine Information im aktuellen Block
# - Neuer Hashwert kann nur mühsam erzeugt werden
# - Dezentralsierung mit Konsensprinzip
##################################################################################################################################

from datetime import datetime
import hashlib

class Block:
    def __init__(self, previous_hash, data):
        self.data = data # Dictionary
        self.previous_hash = previous_hash # Hashwert vom Vorgängerblock
        self.time_stamp = datetime.now()
        self.proof_of_work = 0
        self.hash = self.calculate_hash() # Hashwert für aktuellen Block
       
    def calculate_hash(self):
        data = str(self.previous_hash) + \
        str(self.data) + \
        str(self.time_stamp) + \
        str(self.proof_of_work)
        return hashlib.sha256(data.encode()).hexdigest()

    def mine(self, difficulty): # damit wird einfach Zeit verbarucht, um den Hashwert für einen Block neu zu berechnen => komplette Blockchain kann so nicht einfach neu berechnet werden
        while  not self.hash.startswith("0" * difficulty):
            self.proof_of_work += 1
            self.hash = self.calculate_hash()  

class Blockchain:
    def __init__(self):
        genesis_block = Block("0", {"is_genesis": True})
        self.chain = [genesis_block] # Genesis Block als ersten Block einfügen

    def add_block(self, data):
        last_block = self.chain[-1]
        new_block = Block(last_block.hash, data)    
        new_block.mine(5) # find a hash for new block
        self.chain.append(new_block)

    def is_valid(self): # prüft, ob die Blockchain noch konsistent ist
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash(): # aktueller Block wurde verändert
                return False
            if current_block.previous_hash != previous_block.hash: # Vorgängerblock wurde verändert => er hat jetzt einen Hashwert, der nicht mehr dem im aktuellen Block entspricht
                return False
        return True

    def show_blockchain(self):
        print("\nShow Blockchain:")
        for i in blockchain.chain:
            print("-" * 30)
            print(i.data)
            print(i.hash)
            print(i.previous_hash)
            print(i.time_stamp)
            print(i.proof_of_work)
        print("-" * 30)
   
blockchain = Blockchain()
blockchain.add_block({"from": "Viet", "to": "David", "amount": 100})
blockchain.add_block({"from": "Adam", "to": "Beck", "amount": 150})
blockchain.add_block({"from": "Adam", "to": "Reto", "amount": 250})
blockchain.show_blockchain()
print("\nCheck Blcokchain:", blockchain.is_valid())
blockchain.chain[3].data["amount"] = 1000000 # Hack
blockchain.show_blockchain()
print("\nCheck Blcokchain:", blockchain.is_valid())
