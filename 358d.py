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

            print(f"{self.name} attacks! Health now: {self.health, self.armor}")


        else:

            print(f"{self.name} is too tired to attack. Health: {self.health, self.armor}")

    def action(self, warrior1):

        if self.health >= 10:

            self.health -= 30

            print(f"{self.name} attacks! now: {self.health, self.armor}")


        else:

            print(f"{self.name} is too tired to attack. Health: {self.health, self.armor}")

    def take_damage(self, damage):

        if armor < 0:
            health = randint(10, 20)

        if endurance < 0:
            health = randint(0, 10)

        else:
           health_loss = random.randint(10, 30)
           self.health -= health_loss
            
        if self.health < 0:
            self.health = 0

            print(f"Warrior loses {health_loss} health points. Current health: {self.health}")





