import rrd_getdata
import datetime

print '#####################################################################################################'
print 'INICIO'
#get current time
date1 = datetime.datetime.now()
date1 = date1.replace(microsecond=0)
print 'timestamp: ' + str(date1)

rrd_getdata.insert_data()


print 'FIM'