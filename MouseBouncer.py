import random
import mouse

looper = True
SideSwitcher = True

while looper == True:
    Ender = random.randint(1, 5)
    y1 = random.randint(1, 1080)
    y2 = random.randint(1, 1080)

    if SideSwitcher == True:
        mouse.move(1, y1, True, 2)
        SideSwitcher = False

    if SideSwitcher == False:
        mouse.move(1920, y2, True, 2)
        SideSwitcher = True

    