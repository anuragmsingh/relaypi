##This program displays a moving continuous sequence of HIGH pins. Sequence length is incremented after each iteration

import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TIME_SLICE = 100
if(len(sys.argv)>1 and sys.argv[1].isdigit()):
    TIME_SLICE = int(sys.argv[1])

ONE_SEC = 1
ONE_MSEC = 0.001

pinState=[1, 1, 1, 1, 1, 1, 1, 1]
pinList = [26, 19, 13, 6, 5, 11, 9, 10]
pinListLen = len(pinList)

def setLow(idx):
    GPIO.output(idx, GPIO.LOW)

def setHigh(idx):
    GPIO.output(idx, GPIO.HIGH)

def mapBitToPin(num):
    for idx in range(0, pinListLen):
        if(num&(1<<idx)):
            if(pinState[idx]):
                pinState[idx]=0
                setLow(pinList[idx])
        else:
            if(not pinState[idx]):
                pinState[idx]=1
                setHigh(pinList[idx])

    time.sleep(TIME_SLICE*ONE_MSEC)

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    setHigh(i)

time.sleep(TIME_SLICE*ONE_MSEC)

try:
    for bitCnt in range(1, pinListLen):
        currVal = (1<<bitCnt)-1
        while ((1<<pinListLen)-1)&currVal:
            mapBitToPin(currVal)
            currVal = currVal<<1
            time.sleep(TIME_SLICE*ONE_MSEC)

    time.sleep(TIME_SLICE*ONE_MSEC)

except KeyboardInterrupt:
  print "Keyboard Interrupt!"

# Reset GPIO settings
GPIO.cleanup()

