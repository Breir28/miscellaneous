# ================
# Facade Pattern
# ================

# Zweck: Bietet eine vereinfachte Schnittstelle zu einem komplexen Subsystem.
# Verwendung: Nützlich, um die Komplexität eines Systems zu verbergen und eine einfache Schnittstelle bereitzustellen.

# Komplexes Subsystem
class CPU:
    def execute(self):
        print("CPU: Executing instructions.")

class Memory:
    def load(self):
        print("Memory: Loading data.")

class HardDrive:
    def read(self):
        print("Hard Drive: Reading data.")

# Facade
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        self.cpu.execute()
        self.memory.load()
        self.hard_drive.read()
        print("Computer started.")

# Client-Code
def main():
    # Verwendung der Facade
    computer = ComputerFacade()
    computer.start()

if __name__ == "__main__":
    main()
