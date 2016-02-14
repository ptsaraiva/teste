import time
import random
import temp_int
import phinterface

class sensor():

    def __init__(self):
        self.interface = None

    def get_temp_aqua(self):
        print 'getting aqua temperature'
        #return random.randrange(24,26)

        lines = self.temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.temp_raw()
        temp_output = lines[1].find('t=')

        if temp_output != -1:
            temp_string = lines[1].strip()[temp_output+2:]
            temp_c = round(float(temp_string) / 1000.0,1)
            print temp_c
            return temp_c
        else:
            print 'error reading aqua temp'


    def get_temp_env(self):
        print 'getting environment temperature and humidity'
        #return random.randrange(18,21)
        t, h = temp_int.get_temp2()
        return round (t, 1)

    def get_hum_env(self):
        print 'getting environment humidity'
        #return random.randrange(18,21)
        t, h = temp_int.get_temp2()
        return round (h, 1)

    def get_ph(self):
        print 'getting ph'
        #return round(random.random() + 6.0, 1)
        return round(phinterface.get_ph4(),1)


    def temp_raw(self):
        temp_sensor = "/sys/bus/w1/devices/28-0000062c6479/w1_slave"
        f = open(temp_sensor, 'r')
        lines = f.readlines()
        f.close()
        return lines
