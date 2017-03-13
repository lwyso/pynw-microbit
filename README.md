# pynw-microbit
Python User Group coding session on microbit in MicroPython

![Alt Text](https://github.com/lwyso/pynw-microbit/blob/master/mbpynw.gif)

The BBC Micro:bit is a low cost pocket-sized computer, the device has motion detection, built in compass, bluetooth technology, and quite a few other functions as well. It is for use in teaching computing at schools, and was given to every child in year 7 across the UK in 2016​. 

In the session, we will​ be looking ​at a number of projects​ created by the wider community, followed by a hands on coding session, write your own code in MicroPython, and then a show and tell of your project at the end.

## Writing your code

You can write code online to operate the micro:bit by:

- Using the [online code editor - All options](http://microbit.org/code/)
- [JavaScript Blocks Editor](https://pxt.microbit.org/?lang=en)
- [MicroPython Editor](http://python.microbit.org/editor.html)

Once you are happy with your code, you can save, download and then drag the hex file to the micro:bit!

Alternatively you may want to download a micro editor if you wish to write code offline:

- [Mu - a "micro" editor](https://github.com/mu-editor/mu)

Same with the online editor, once you are happy with your code, you can save and REPL to the micro:bit!

## Getting started

## Example Code

All micro:bit are preload with an example of the game 'Magic 8', sample code from [BBC micro:bit MicroPython documentation - Accelerometer](https://microbit-micropython.readthedocs.io/en/latest/accelerometer.html).

```
from microbit import *
import random

answers = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it"
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]

while True:
    display.show("8")
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(1000)
        display.scroll(random.choice(answers))
```