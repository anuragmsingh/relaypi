#This program makes diametric opposite switches to rotate.

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

def oppPOS(pos):
    return (pos+(pinListLen>>1))%pinListLen

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    setHigh(i)

time.sleep(TIME_SLICE*ONE_MSEC)

try:

    iterate=5
    while iterate:

        iterate = iterate - 1
        for pos in range(0, pinListLen>>1):
            oppPos = oppPOS(pos)
            setLow(pinList[pos])
            setLow(pinList[oppPos])
            setHigh(pinList[(pos-1)%pinListLen])
            setHigh(pinList[(oppPos-1)%pinListLen])

            time.sleep(TIME_SLICE*ONE_MSEC)

        for pos in range((pinListLen>>1)-1, -1, -1):
            oppPos = oppPOS(pos)
            setLow(pinList[pos])
            setLow(pinList[oppPos])
            setHigh(pinList[(pos+1)%pinListLen])
            setHigh(pinList[(oppPos+1)%pinListLen])

            time.sleep(TIME_SLICE*ONE_MSEC)

    time.sleep(TIME_SLICE*ONE_MSEC)

except KeyboardInterrupt:
  print "Keyboard Interrupt!"

# Reset GPIO settings
GPIO.cleanup()
