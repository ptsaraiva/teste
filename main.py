__author__ = 'Paulo'

import RPi.GPIO as GPIO
import time
import json
import plotly.plotly as py
from plotly.graph_objs import *

import datetime
import random

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


py.sign_in("ptsaraiva", "g5xd13nl4n")



for i in range (5):
    date = datetime.datetime.now()
    temp_env = random.randrange(17.0,24.0)
    temp_aqua = temp_env + 2

    temperature_env = Scatter(
        y=[temp_env],
        x=[date],
        name = 'temperatura ambiente'
    )

    temperature_aqua = Scatter(
        y=[temp_aqua],
        x=[date],
        name = 'temperatura aquario'
    )

    data = Data([temperature_env, temperature_aqua])

    # Take 1: if there is no data in the plot, 'extend' will create new traces.
    plot_url = py.plot(data, filename='temperature', fileopt='extend')

    time.sleep(2)

