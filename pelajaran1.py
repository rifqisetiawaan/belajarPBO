class Hero:
    def __init__(self, name, health, attackPower):
        self.nama = name
        self.health = health
        self.attack = attackPower

    def printNama(self):
        print("nama Saya adalah " + self.nama + " darah saya " + str(self.health) + " serangan saya " + str(self.attack))

sniper = Hero("Sniper", 100, 50)
marksmen = Hero("Marksmen", 100, 50)

sniper.printNama()
marksmen.printNama()