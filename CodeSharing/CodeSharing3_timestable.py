# Generate a random number and progress through times table on button b
from microbit import *
import random
 
# Generate the variables
times = (random.randint(1, 12))
multiplyer = 2
display.scroll(str('Your times table is : '))
 
# Times table function
def times_table(times, multiplyer):
    display.scroll(str(times))
    while True:
        if button_b.is_pressed():
            display.scroll(str(times * multiplyer))
            multiplyer += 1
        elif button_a.is_pressed():
            multiplyer -= 1
            display.scroll(str(times * multiplyer))
           
# re run the program on button a
times_table(times, multiplyer)