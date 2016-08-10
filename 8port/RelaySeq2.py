##This program completes a loop of single open switch forward then backward for each index

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
    print "[", pinList.index(idx), "] -- LOW"
    GPIO.output(idx, GPIO.LOW)

def setHigh(idx):
    print "[", pinList.index(idx), "] -- HIGH"
    GPIO.output(idx, GPIO.HIGH)

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    setLow(i)

try:
    maxCount = 2*pinListLen
    currCount = 0

    while(currCount<maxCount):

        position = currCount%pinListLen

        time.sleep(TIME_SLICE*ONE_MSEC)

        setHigh(pinList[position])
        for i in range(pinListLen):
            time.sleep(TIME_SLICE*ONE_MSEC)
            setLow(pinList[position])
            position = (position+1)%pinListLen
            setHigh(pinList[position])
        time.sleep(TIME_SLICE*ONE_MSEC);
        setLow(pinList[position])

        time.sleep(TIME_SLICE*ONE_MSEC)

        #Switch Dir

        setHigh(pinList[position])
        for i in range(pinListLen):
            time.sleep(TIME_SLICE*ONE_MSEC)
            setLow(pinList[position])
            position = (position-1)%pinListLen
            setHigh(pinList[position])
        time.sleep(TIME_SLICE*ONE_MSEC)
        setLow(pinList[position])

        currCount = currCount + 1

except KeyboardInterrupt:
  print "Keyboard Interrupt!"

# Reset GPIO settings
GPIO.cleanup()

