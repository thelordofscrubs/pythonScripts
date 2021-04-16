import random

guns = ["Knife", "Classic","Shorty","Frenzy","Ghost","Sheriff","Stinger","Spectre","Bucky","Judge","Bulldog","Guardian","Phantom","Vandal","Marshal","Operator","Ares","Odin"]

usedGuns = []

currentGun = ""

def getGun():
    currentGun = guns.pop(random.randint(0,len(guns)-1))
    usedGuns.append(currentGun)
    print("Current gun is: " + currentGun+"\n")

while True:
    print("Press enter to get the next gun, or enter 'N' to stop the program")
    if (input() == ""):
        getGun()
    else:
        break
    if len(guns) == 0:
        guns =  usedGuns.copy()
        usedGuns = []