from random import randint, random
from tkinter.font import names
from xml.dom.minidom import ProcessingInstruction


class Warrior:
    def __init__(self, name, health, damage,endurance, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.endurance = endurance
        self.armor = armor
        print( self.name,self.health, self.endurance, self.damage, self.armor)

    def Attack1(self, warrior):
        warrior.health -= warrior.damage
        warrior.endurance -= warrior.damage
        warrior.armor -= warrior.damage

        print ("voin", self.name,"atakuet voina", warrior.name + ".")
        print(" U Voina", warrior.name, "ostaetsya", warrior.health, "zdorov''ya!")

John = Warrior("John", 100, endurance=randint (0, 10),
Vasya = Warrior("Vasya", 100,randint (0,10))
               while (John.health > 0 and Vasya.health > 0):
                    Vasya.Attack1(John)



    def Defend(self, warrior):
        warrior.health -= warrior.damage
        warrior.endurance -= warrior.damage
        warrior.armor-= warrior.damage

John = Warrior("John", 100,randint (0, 20), armor=randint (0, 10))
Vasya = Warrior("Vasya", 100,randint (0,20), armor=randint (0, 10))

    def Attack1(self, warrior):
        warrior.health -= warrior.damage
        warrior.endurance -= warrior.damage
        warrior.armor -= warrior.damage

John = Warrior("John", 100, randint(0, 30),endurance=randint (0, 10))
Vasya = Warrior("Vasya", 100, randint(0, 30))

John = Warrior("John",armor=0)
Vasya = Warrior("Vasya",armor=0)






