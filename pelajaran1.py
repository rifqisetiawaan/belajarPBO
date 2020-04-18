class Hero:
    def __init__(self, name):
        self.nama = name

    def printNama(self):
        print("nama Saya adalah " + self.nama)

sniper = Hero("sniper")

sniper.printNama()