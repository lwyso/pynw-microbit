# pynw-microbit
Python User Group coding session on microbit in MicroPython

![Alt Text](https://github.com/lwyso/pynw-microbit/blob/master/mbhellopynw.gif)

The BBC Micro:bit is a low cost pocket-sized computer, the device has motion detection, built in compass, bluetooth technology, and quite a few other functions as well. It is for use in teaching computing at schools, and was given to every child in year 7 across the UK in 2016​. 



In the session, we will​ be looking ​at a number of projects​ created by the wider community, followed by a hands on coding session, write your own code in MicroPython, and then a show and tell of your project at the end.

## What is Micro:bit?

- [Introducing the BBC micro:bit](http://www.bbc.co.uk/programmes/p03kn22r) - Watch this short animation to find out more about the BBC micro:bit and its features.
- [BBC Micro:Bit Hands On | WIRED](https://www.youtube.com/watch?v=k6YfP7dRP5Q) An overview of the BBC Micro:bit by Wired.

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

There are a number of web sites, documentations, guides and projects to get started, here are a few suggestions:

- [BBC micro:bit MicroPython documentation](https://microbit-micropython.readthedocs.io/en/latest/index.html) - This web site includes a number of tutorials you need to get started from basic Micropython code to advanced API.

- Stuck on an idea? Why not visit the ideas page [Play, learn, explore](http://microbit.org/ideas/).

- Live lesson videos from the [BBC micro:bit Live Lesson](http://www.bbc.co.uk/programmes/articles/2M3H2YpKLsw2W8fC2ycHYSR/welcome-to-the-micro-bit-live-lesson).

## Your task

- Create a game! or
- Build something useful?

## Code sharing - show and tell
At the end of the workshop we had a number of show and tell, below are the links to their code. Thanks for sharing.

- [Diamond or Square?](https://github.com/lwyso/pynw-microbit/blob/master/CodeSharing/CodeSharing1_diamondORsquare.py)
- [Random Pixel](https://github.com/lwyso/pynw-microbit/blob/master/CodeSharing/CodeSharing2_randompixel.py)
- [Times table](https://github.com/lwyso/pynw-microbit/blob/master/CodeSharing/CodeSharing3_timestable.py)
- [Step...](https://github.com/lwyso/pynw-microbit/blob/master/CodeSharing/CodeSharing4_step.py)

## Example Code

All micro:bit are pre-loaded with an example of the game 'Magic 8', sample code from [BBC micro:bit MicroPython documentation - Accelerometer](https://microbit-micropython.readthedocs.io/en/latest/accelerometer.html).
Sample code can be downloaded here (right click save link as...), [magic8.py](https://github.com/lwyso/pynw-microbit/blob/master/SampleCode/magic8.py) or [magic8.hex](https://github.com/lwyso/pynw-microbit/blob/master/SampleCode/magic8.hex) to load straight to your micro:bit.

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