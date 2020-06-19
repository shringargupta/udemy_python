import random


playerhp = 260
enemyatkh = 80
enemyatkl = 60

"""
while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <=0:
        playerhp = 0
    print("Enemy strikes for", dmg, "points of damage,", "Current HP is", playerhp)

    if playerhp == 0:
        print("You have DIED, you can not respawn as you are dead")
"""
#CONTINOUS WHILE LOOP and then using break to stop it

"""
while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30
    print("Enemy strikes for", dmg, "points of damage,", "Current HP is", playerhp)

    if playerhp == 30:
        print("You have low health, you have been transported to nearest Inn")
        break
"""

# Continue statement
""" 
    to create an empty block of code use Pass statement 
"""

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