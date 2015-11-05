import smbus
import temp_int


opampGain = 5.25
pH7Cal = 2048.0  #assume ideal probe and amp conditions 1/2 of 4096
pH4Cal = 1286.0  #using ideal probe slope we end up this many 12bit units away on the 4 scale
pHStep = 59.16 #ideal probe slope
vRef = 4.096

I2C_ADDRESS = 0x48

bus = smbus.SMBus(1)

def get_ph1():

    print 'get_ph1: '
    #Set all ports in input mode
    #bus.write_byte(I2C_ADDRESS,1)

    #Read all the unput lines
    value1=bus.read_byte(I2C_ADDRESS)
    #print value1
    value2=bus.read_byte(I2C_ADDRESS)
    #print value2

    #adc_result = value1
    adc_result =  (value1 * 256) + value2
    print 'adc_result: ' + str(adc_result)


    miliVolts = ((adc_result/4096.0)*vRef)*1000.0
    #print 'miliVolts: ' + str(miliVolts)

    temp = ((((vRef*pH7Cal)/4096.0)*1000.0)- miliVolts)/opampGain
    pH = 7-(temp/pHStep)

    print 'pH: ' + str(pH)

    return pH


def get_ph2():
    print 'get_ph2: '

    data = []
    data_aux = []

    bus = smbus.SMBus(1)
    data = bus.read_i2c_block_data(I2C_ADDRESS, 1,32)
    #print data

    #print len(data)
    for x in range (0,len(data)-1, 2):
        #print str(x) + ' : ' + str(data[x]) + '.' + str(data[x+1])
        val = (data[x] << 8) + data[x+1]
        #print val
        data_aux.append(val)

    #median value
    val = sum(data_aux)/len(data_aux)
    print val

    adc_result = val

    miliVolts = ((adc_result/4096.0)*vRef)*1000.0
    #print 'miliVolts: ' + str(miliVolts)

    temp = ((((vRef*pH7Cal)/4096.0)*1000.0)- miliVolts)/opampGain
    pH = 7-(temp/pHStep)

    print 'pH: ' + str(pH)

    return pH


def get_ph3():
    print 'get_ph3: '

    ADC7 = 2048.0
    ADC4 = 1270.0

    ph4 = 4.0
    ph7 = 6.86

    data = []
    data_aux = []

    bus = smbus.SMBus(1)
    data = bus.read_i2c_block_data(I2C_ADDRESS, 1,32)
    #print data

    #print len(data)
    for x in range (0,len(data)-1, 2):
        #print str(x) + ' : ' + str(data[x]) + '.' + str(data[x+1])
        val = (data[x] << 8) + data[x+1]
        #print val
        data_aux.append(val)

    #print data_aux

    #median value
    val = sum(data_aux)/len(data_aux)
    print val

    adc_result = val

    miliVolts = ((adc_result*vRef)/4096.0)*1000.0
    #print 'miliVolts: ' + str(miliVolts)

    m = ((ADC7 - ADC4)*vRef*1000)/((ph7-ph4)*opampGain*4096)
    vA = (((ADC4*vRef)/4096.0)*1000.0)/opampGain
    v = miliVolts/opampGain

    pH = (v-vA)/m + ph4
    print 'pH: ' + str(pH)

    return pH

def get_ph4():
    print 'get_ph4: '

    ADC7 = 1950.0
    ADC4 = 1270.0

    ph4 = 4.0
    ph7 = 6.86

    data = []
    data_aux = []

    bus = smbus.SMBus(1)
    data = bus.read_i2c_block_data(I2C_ADDRESS, 1,32)
    #print data

    #print len(data)
    for x in range (0,len(data)-1, 2):
        #print str(x) + ' : ' + str(data[x]) + '.' + str(data[x+1])
        val = (data[x] << 8) + data[x+1]
        #print val
        data_aux.append(val)

    #print data_aux

    #median value
    val = sum(data_aux)/len(data_aux)
    print val

    adc_result = val

    miliVolts = ((adc_result*vRef)/4096.0)*1000.0
    #print 'miliVolts: ' + str(miliVolts)

    m = ((ADC7 - ADC4)*vRef*1000)/((ph7-ph4)*opampGain*4096)
    print 'm: ' + str(m)
    vA = (((ADC4*vRef)/4096.0)*1000.0)/opampGain
    v = miliVolts/opampGain

    pH = (v-vA)/m + ph4
    print 'pH: ' + str(pH)

    return pH





