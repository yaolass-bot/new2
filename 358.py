class Warrior:
    def __init__(self, name, stamina):
        self.name = name
        self.stamina = stamina

    def attack(self):
        if self.stamina >= 10:
            self.stamina -= 0
            print(f"{self.name} attacks! Stamina now: {self.stamina}")
        else:
            print(f"{self.name} is too tired to attack. Stamina: {self.stamina}")


    def defence(self):
        if self.health >= 10:
            self.health -= 20
        if self.armor >= 0:
            self.armor -= 10

            print(f"{self.name} attacks! Health now: {self.health,self.armor}")
        else:
            print(f"{self.name} is too tired to attack. Health: {self.health,self.armor}")

    def action(self,warrior1):
        if self.health >= 10:
            self.health -= 30

            print(f"{self.name} attacks! now: {self.health, self.armor}")
        else:
            print(f"{self.name} is too tired to attack. Stamina: {self.health, self.armor}")



