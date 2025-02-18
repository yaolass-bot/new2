from random import randint

from time import sleep

players =  {
    1 : ['Shawn', 0, 100],
    2 : ['Bob', 0, 100],
}

players = players.get(randint(1, len(players)))
print(players)




