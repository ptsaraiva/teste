import sensorInterface

my_sens = sensorInterface.sensor()

temp_aqua = my_sens.get_temp_aqua()
temp_env = my_sens.get_temp_env()

print ' | temp_aqua: ' + str(temp_aqua) + ' | temp_env: ' + str(temp_env)