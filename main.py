__author__ = 'Paulo'

#import RPi.GPIO as GPIO
#import time
#import json
#import plotly
import plotly.plotly as py
import plotly.tools as tls
#from plotly.graph_objs import *

import publicar as pub
import plotlyInterface as pInt

import phinterface

import datetime
#import random

#################################################
#teste pinout

# print 'ola'
#
# pin = 19
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(pin, GPIO.OUT)
#
# GPIO.output(pin, True)
# time.sleep(0.5)
# GPIO.output(pin, False)
# time.sleep(0.5)
#
# print 'fim'
#
# GPIO.cleanup()


####################################################
#usar funcao:
#py.sign_in(c["username"], c["api_key"])
#pub.publica_plot()

#####################################################
#usar classes:
#p = plotlyInterface.plotlyInterface()
p = pInt.plotlyInterface()
p.setup()
p.plotData_extend("data aqua")


####################################################
# for i in range(5):
#     pub.publica_plot()
#     time.sleep(1)