class Hero:
    def __init__(self, name, health, attackPower, armor):
        self.nama = name
        self.health = health
        self.attack = attackPower
        self.armor = armor

    def printNama(self):
        print("nama Saya adalah " + self.nama + " darah saya " + str(self.health))
        print("serangan saya " + str(self.attack) + " armor saya " + str(self.armor))
        print("\n")

    def serang(self, lawan):
        print(self.nama + " menyerang " + lawan.nama)


sniper = Hero("Sniper", 100, 50, 5)
marksmen = Hero("Marksmen", 100, 50, 5)

sniper.printNama()
marksmen.printNama()