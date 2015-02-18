#!/usr/bin/python
import Adafruit_DHT

def get_temp():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
    print str(humidity) + '% | ' + str(temperature)
    if temperature < 12:
        print "ERRO de leitura"
        temperature *= 2

    return (temperature, humidity)