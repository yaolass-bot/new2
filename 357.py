class Warrior:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0


def battle(warrior1, warrior2):
    round_number = 1
    while warrior1.is_alive() and warrior2.is_alive():
        print(f"Round {round_number}:")
        print(f"{warrior1.name} attacks {warrior2.name} for {warrior1.attack} damage.")
        print(f"{warrior2.name} attacks {warrior1.name} for {warrior2.attack} damage.")

        warrior1.take_damage(warrior2.attack)
        warrior2.take_damage(warrior1.attack)

        print(f"{warrior1.name} has {warrior1.health} health left.")
        print(f"{warrior2.name} has {warrior2.health} health left.")
        print("-" * 30)

        round_number += 1

    if warrior1.is_alive():
        print(f"{warrior1.name} wins!")
    elif warrior2.is_alive():
        print(f"{warrior2.name} wins!")
    else:
        print("It's a draw!")


# Example usage
warrior1 = Warrior("Warrior A", 100, 20)
warrior2 = Warrior("Warrior B", 100, 20)

battle(warrior1, warrior2)


    


