import random

"""
    Class is a blue print for the objects, so rather than creating functions
    and variables that will be used throughout
    again and again they are declared in class
"""
""" # CLASS AND OBJECTS
class Enemy:

    # init runs when the class has been instantiated
    # or when an object has been created from this class
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print(self.atkl)

enemy1 = Enemy(40,90) # instantiation of the class
enemy1.getAtk()

enemy2 = Enemy(70,85)
enemy2.getAtk()
"""

"""
    Instance variable:
        A variable that is different or can be different
        for every instance of the class
"""
class Enemy:
    
    hp = 100
    # init runs when the class has been instantiated
    # or when an object has been created from this class
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print("atk is",self.atkl)

    def getHp(self):
        print("Hp is", self.hp)

enemy1 = Enemy(40,90) # instantiation of the class
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(70,85)
enemy2.getAtk()
enemy2.getHp()
"""
playerhp = 260
enemyatkh = 80
enemyatkl = 60


while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30
    print("Enemy strikes for", dmg, "points of damage,", "Current HP is", playerhp)

    if playerhp > 30:
        continue # ignores everything after this statement and begins from starting again

    print("You have low health, you have been transported to nearest Inn")
    break
"""