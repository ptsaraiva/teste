import smbus


opampGain = 5.25
pH7Cal = 2048.0  #assume ideal probe and amp conditions 1/2 of 4096
pH4Cal = 1286.0  #using ideal probe slope we end up this many 12bit units away on the 4 scale
pHStep = 59.16 #ideal probe slope
vRef = 4.096;

I2C_ADDRESS = 0x48

bus = smbus.SMBus(1)

#Set all ports in input mode
#bus.write_byte(I2C_ADDRESS,1)

#Read all the unput lines
value1=bus.read_byte(I2C_ADDRESS)
print value1
value2=bus.read_byte(I2C_ADDRESS)
print value2

#adc_result = value1
adc_result =  (value1 * 256) + value2
print 'adc_result: ' + str(adc_result)


miliVolts = ((adc_result/4096.0)*vRef)*1000.0
print 'miliVolts: ' + str(miliVolts)

temp = ((((vRef*pH7Cal)/4096.0)*1000.0)- miliVolts)/opampGain
pH = 7-(temp/pHStep)

print 'pH: ' + str(pH)


print '---------'

bus = smbus.SMBus(1)
data = bus.read_i2c_block_data(I2C_ADDRESS, 5)
print data
val = (data[0] << 8) + data[1]
print val

adc_result = val

miliVolts = ((adc_result/4096.0)*vRef)*1000.0
print 'miliVolts: ' + str(miliVolts)

temp = ((((vRef*pH7Cal)/4096.0)*1000.0)- miliVolts)/opampGain
pH = 7-(temp/pHStep)

print 'pH: ' + str(pH)