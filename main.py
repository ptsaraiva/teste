__author__ = 'Paulo'

import RPi.GPIO as GPIO
import time
import json
#import plotly.plotly as py

print 'ola'

pin = 19
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, True)
time.sleep(5)
GPIO.output(pin, False)
time.sleep(5)

print 'fim'

GPIO.cleanup()
