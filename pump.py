
import RPi.GPIO as GPIO
import time
import datetime

GPIO.cleanup()
pin1 = 18
pin2 = 16

print(GPIO.VERSION)
GPIO.setmode(GPIO.BOARD)

t= 5

time.sleep(t)
print 'a'
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

time.sleep(t)
print 'inicio'


print str(datetime.datetime.now().replace(microsecond=0))
GPIO.output(pin1, GPIO.LOW)
GPIO.output(pin2, GPIO.LOW)
time.sleep(t)

print str(datetime.datetime.now().replace(microsecond=0))
GPIO.output(pin1, GPIO.HIGH)
GPIO.output(pin2, GPIO.HIGH)
time.sleep(t)

print str(datetime.datetime.now().replace(microsecond=0))
GPIO.output(pin1, GPIO.LOW)
GPIO.output(pin2, GPIO.LOW)
time.sleep(t)

print 'fim'

GPIO.cleanup()

