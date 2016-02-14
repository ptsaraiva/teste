import rrdtool
import sensorInterface
import time



def insert_data():

    timestamp = time.time()
    mysensor = sensorInterface.sensor()

    t_env = mysensor.get_temp_env()
    hum = mysensor.get_hum_env()
    t_aqua = mysensor.get_temp_aqua()
    ph = mysensor.get_ph()


    print t_env, t_aqua
    print timestamp
    print ph

    rrdtool.update("/home/pi/teste/aquamonitor_db.rrd","%d:%s:%s:%s:%s" % (timestamp, t_env, hum, t_aqua, ph))



    return


