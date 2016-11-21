#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ansteuerung eines bipolaren 4 Phasen-Schrittmotors (28BYJ-48 mit einem ULN2003 Controller Board
"""
Spannung :5VDC
Phasen : 4
Übersetznug (Speed Variation Ratio) : 1/64 
Schrittwinkel:(5.625°) (64 Schritte/Umdrehung)
1Rotation 64*8=512
Drehmoment: 34.4 mN*m(120 Hz)
"""
import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)

ControlpinX = [06,13,19,26]
ControlpinY = [12,16,20,21]
ControlpinZ = [18,23,24,25]

for pin in(ControlpinX, ControlpinY, ControlpinZ):
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,0)



"""
step               1 2 3 4 5 6 7 8
                   . . . . . . . .
pin 18/12/06       x x           x
pin 23/16/13         x x x        
pin 24/20/19             x x x    
pin 25/21/26                 x x x

"""
seq = [ [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1] ]

def forward_X(steps_X, delay):
    for i in range (steps_X):
        for halfstep in (range (8)):
            for pin in range(4):
                GPIO.output(ControlpinX[pin], seq[halfstep][pin])
            time.sleep(delay)
def forward_Y(steps_Y, delay):
    for i in range (steps_Y):
        for halfstep in (range (8)):
            for pin in range(4):
                GPIO.output(ControlpinY[pin], seq[halfstep][pin])
            time.sleep(delay)        
def forward_Z(steps_Z, delay):
    for i in range (steps_Z):
        for halfstep in (range (8)):
            for pin in range(4):
                GPIO.output(ControlpinZ[pin], seq[halfstep][pin])
            time.sleep(delay)
def backwards_X(steps_nX, delay):
    for i in range (steps_nX):
        for halfstep in reversed(range (8)):
            for pin in range(4):
                GPIO.output(ControlpinX[pin], seq[halfstep][pin])       
            time.sleep(delay)
def backwards_Y(steps_nY, delay):
    for i in range (steps_nY):
        for halfstep in reversed(range (8)):
            for pin in range(4):
                GPIO.output(ControlpinY[pin], seq[halfstep][pin])       
            time.sleep(delay)
def backwards_Z(steps_nZ, delay):
    for i in range (steps_nZ):
        for halfstep in reversed(range (8)):
            for pin in range(4):
                GPIO.output(ControlpinZ[pin], seq[halfstep][pin])
            time.sleep(delay)
def off_X(False):
    for pin in(ControlpinX):
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,0)
def off_Y(False):
    for pin in(ControlpinY):
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,0)
def off_Z(False):
    for pin in(ControlpinZ):
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,0)

if __name__== '__main__':
    try:
        while True:
            delay = raw_input("Zeitverzogerung (7~1000) = ")
            steps_X = raw_input("+X: Wie viele Schritte = ")
            steps_Y = raw_input("+Y: Wie viele Schritte = ")
            steps_Z = raw_input("+Z: Wie viele Schritte = ")
            steps_nX = raw_input("-X: Wie viele Schritte = ")
            steps_nY = raw_input("-Y: Wie viele Schritte = ")
            steps_nZ = raw_input("-Z: Wie viele Schritte = ")
            forward_X(int(steps_X), float(delay)/10000)
            off_X(False)
            forward_Y(int(steps_Y), float(delay)/10000)
            off_Y(False)
            forward_Z(int(steps_Z), float(delay)/10000)
            off_Z(False)
            backwards_X(int(steps_nX), float(delay)/10000)
            off_X(False)
            backwards_Y(int(steps_nY), float(delay)/10000)
            off_Y(False)
            backwards_Z(int(steps_nZ), float(delay)/10000)
            off_Z(False)
            
                                 

           

                
    
    except KeyboardInterrupt:

       print("Programm vom User gestoppt")
       GPIO.cleanup()        

