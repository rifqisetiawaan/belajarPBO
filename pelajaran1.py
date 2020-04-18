class Hero:
    def __init__(self, name, health):
        self.nama = name
        self.health = health

    def printNama(self):
        print("nama Saya adalah " + self.nama + " darah saya " + str(self.health))

sniper = Hero("Sniper", 100)
marksmen = Hero("Marksmen", 100)

sniper.printNama()
marksmen.printNama()