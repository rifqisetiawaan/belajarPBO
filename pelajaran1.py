class Hero:
    def __init__(self, name, health):
        self.nama = name
        self.health = health

    def printNama(self):
        print("nama Saya adalah " + self.nama + " darah saya " + str(self.health))

sniper = Hero("sniper", 100)

sniper.printNama()