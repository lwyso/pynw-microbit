from microbit import *
import random
image_list = [Image.DIAMOND, Image.SQUARE]
 
while True:
   if button_a.is_pressed() and button_b.is_pressed():
        score = 0
        for i in range(10):
            choice = random.choice(image_list)
            display.show(choice)
            while not(button_a.is_pressed()) and not(button_b.is_pressed()):
                sleep(1)
            if button_a.is_pressed() and choice == Image.DIAMOND:
                score = score+1
            elif button_b.is_pressed() and choice == Image.SQUARE:
                score = score+1
            display.clear()
           
        display.scroll("Your score is " + str(score))