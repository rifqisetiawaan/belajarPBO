class Hero:
    def __init__(self, name, health, attackPower, armor):
        self.name = name
        self.health = health
        self.attack = attackPower
        self.armor = armor

    def printNama(self):
        print("nama Saya adalah " + self.name + " darah saya " + str(self.health))
        print("serangan saya " + str(self.attack) + " armor saya " + str(self.armor))
        print("\n")

    def serang(self, lawan):
        print(self.name + " menyerang " + lawan.nama)
        lawan.diserang(self)

    def diserang(self, lawan, attackPower_lawan):
        print(self.name + " diserang " + lawan.nama)
        attack_diterima = attackPower_lawan / self.armor
        print("Serangan Terasa " + str(attack_diterima))


sniper = Hero("Sniper", 100, 50, 5)
marksmen = Hero("Marksmen", 100, 50, 5)

sniper.printNama()
marksmen.printNama()