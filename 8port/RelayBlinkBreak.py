##This program completes a FORWARD loop followed by a BACKWARD loop at each present index

import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TIME_SLICE = 100
if(len(sys.argv)>1 and sys.argv[1].isdigit()):
    TIME_SLICE = int(sys.argv[1])

ONE_SEC = 1
ONE_MSEC = 0.001

pinList = [26, 19, 13, 6, 5, 11, 9, 10]
pinListLen = len(pinList)

def setLow(idx):
    GPIO.output(idx, GPIO.LOW)

def setHigh(idx):
    GPIO.output(idx, GPIO.HIGH)

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    setHigh(i)

try:
    count = 2

    while count:

        count = count-1
        time.sleep(TIME_SLICE*ONE_MSEC)

        for i in pinList:
            GPIO.setup(i, GPIO.OUT)
            setLow(i)

        time.sleep(TIME_SLICE*ONE_MSEC)

        for i in pinList:
            GPIO.setup(i, GPIO.OUT)
            setHigh(i)

except KeyboardInterrupt:
  print "Keyboard Interrupt!"

# Reset GPIO settings
GPIO.cleanup()

