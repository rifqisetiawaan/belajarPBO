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
        print(self.name + " menyerang " + lawan.name)
        lawan.diserang(self, self.attack)
        print("\n")

    def diserang(self, lawan, attackPower_lawan):
        print(self.name + " diserang " + lawan.name)
        attack_diterima = attackPower_lawan / self.armor
        print("Serangan Terasa " + str(attack_diterima))
        self.health -= attack_diterima
        print("darah " + self.name + " tersisa " + str(self.health))


sniper = Hero("Sniper", 100, 50, 5)
marksmen = Hero("Marksmen", 100, 50, 5)

print(sniper.__dict__)
print(marksmen.__dict__)
print("\n")
sniper.serang(marksmen)
marksmen.serang(sniper)