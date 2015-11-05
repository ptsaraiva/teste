import phinterface
import temp_int
import threading
import time

def f():
    phinterface.get_ph4()
    ##threading.Timer(15, f).start()


#phinterface.get_ph1()
phinterface.get_ph2()
phinterface.get_ph3()
phinterface.get_ph4()

t, h = temp_int.get_temp2();
f()

##time.sleep(60)