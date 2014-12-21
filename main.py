__author__ = 'Paulo'

import RPi.GPIO as GPIO
import time
import json
import plotly.plotly as py
import datetime
import random

print 'ola'

pin = 19
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, True)
time.sleep(1)
GPIO.output(pin, False)
time.sleep(1)

print 'fim'

GPIO.cleanup()


with open('./config.json') as config_file:
    plotly_user_config = json.load(config_file)

    py.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])


url = py.plot([
{
    'x': [], 'y': [], 'type': 'scatter',
    'stream': {
        'token': plotly_user_config['plotly_streaming_tokens'][0],
        'maxpoints': 200
    }
}], filename='Raspberry Pi Streaming Example Values')

print "View your streaming graph here: ", url

stream = py.Stream(plotly_user_config['plotly_streaming_tokens'][0])
stream.open()



#the main sensor reading and plotting loop
for i in range(3):

    temp = random.randrange(17.0,24.0)
    print 'time:' + str(datetime.datetime.now()) + ' temp: ' + str(temp)
    # write the data to plotly

    stream.write({'x': datetime.datetime.now(), 'y': temp})

    # delay between stream posts
    time.sleep(5)


