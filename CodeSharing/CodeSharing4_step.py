#### reciever code
 
import serial
ser = serial.Serial("COM3",115200)
while True:
    print(ser.readline())
 
#### micro:bit code
 
from microbit import *
 
uart.init(baudrate=115200)
 
while True:
    while not button_a.is_pressed():
        pass
    while button_a.is_pressed():
        pass
    uart.write("step\n")
    while not button_b.is_pressed():
        pass
    while button_b.is_pressed():
        pass
    uart.write("step")