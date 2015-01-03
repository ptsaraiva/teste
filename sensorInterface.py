import time
import random

class sensor():

    def __init__(self):
        self.interface = None

    def get_temp_aqua(self):
        #return random.randrange(24,26)

        lines = self.temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.temp_raw()
        temp_output = lines[1].find('t=')

        if temp_output != -1:
            temp_string = lines[1].strip()[temp_output+2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c


    def get_temp_env(self):
        return random.randrange(18,21)

    def get_ph(self):
        import random
        return round(random.random() + 6.0, 2)


    def temp_raw(self):
        temp_sensor = "/sys/bus/w1/devices/28-0000062c6479/w1_slave"
        f = open(temp_sensor, 'r')
        lines = f.readlines()
        f.close()
        return lines
