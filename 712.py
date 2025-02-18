
import random

a = 100
b = 100
hit = random.randint(1,20)
alive = True

dmg = random.randint(1,20)
if hit > 20:
    dmg = random.randint(1,8)
print("You hit", "for","dmg")

if hit < 20:
 print ("you hit", "for","dmg")
dmg = 0
mlife = a - dmg

print(mlife,"Hit point left")























