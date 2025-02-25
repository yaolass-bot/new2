


class Warrior:
    def __init__(self, health, hit):
        self.health = 100
        self.hit= 100

    def attack(self, filename):
        print("Attacking " + filename)
        x = self.health - self.hit
        x = x -20
        if x < 0:
            print("Sorry, you are dead")













