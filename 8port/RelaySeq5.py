##This program displays a binary equivalent of seq 1..max

import math
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

def getIndex(val, lsb, isRight):
    idx = int(lsb)
    idx = ((idx-1)%pinListLen, (idx+1)%pinListLen)[isRight]

    if(not val&(1<<idx)):
        return idx;
    return getIndex(val, idx, isRight)

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    setHigh(i)

try:
    initial = 3
    for idx in range(0, pinListLen):

        stateList = []

        time.sleep(TIME_SLICE*ONE_MSEC)

        currVal = initial<<idx
        currVal = (currVal, (1<<(pinListLen-1))^1)[currVal>=1<<pinListLen]
        stateList.append(currVal)
        mapBitToPin(currVal)

        while currVal<(1<<pinListLen)-1:

            lsb = math.floor(math.log(currVal-(currVal&(currVal-1)), 2))
            currVal = currVal^(1<<getIndex(currVal, lsb, True))
            currVal = currVal^(1<<getIndex(currVal, lsb, False))
            stateList.append(currVal)
            mapBitToPin(currVal)

        for state in reversed(stateList):
            mapBitToPin(state)

except KeyboardInterrupt:
  print "Keyboard Interrupt!"

# Reset GPIO settings
GPIO.cleanup()

