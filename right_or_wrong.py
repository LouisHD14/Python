import random

rz = random.randint(0, 6)
starter = input("Tippe 'start' ein um zu starten. ")

def start():
    if rz == 1:
        print("Du hast gewonnen!")
    elif rz == 6:
        print("Loser!")
    else :
        print("Falsche Zahl")


if starter == "start":
    start()
else:
    exit()
