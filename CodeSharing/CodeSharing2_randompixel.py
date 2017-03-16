from microbit import *
import random
 
while True:
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    display.set_pixel(x, y, 9)
    sleep(100)
    display.clear()