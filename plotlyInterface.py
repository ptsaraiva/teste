import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *
import datetime

import sensorInterface

class plotlyInterface():

    def __init__(self):
        self.username = None
        self.api_key = None
        self.setup()


    def setup(self):
        my_cred = tls.get_credentials_file()
        py.sign_in(my_cred['username'], my_cred['api_key'])


    def plotData_extend(self, plot_name):

        #get current time
        date = datetime.datetime.now()
        date = date.replace(microsecond=0)

        #instanciate a sensor object
        my_sens = sensorInterface.sensor()

        #get data from sensors
        temp_aqua = my_sens.get_temp_aqua()
        temp_env = my_sens.get_temp_env() - 5
        ph = my_sens.get_ph()


        #set the data into properly variables
        temperature_env_data = Scatter(
            x = [date],
            y=[temp_env],
            name = 'temperatura ambiente'
        )

        temperature_aqua_data = Scatter(
            x=[date],
            y=[temp_aqua],
            name = 'temperatura aquario'
        )

        ph_data = Scatter(
            x = [date],
            y = [ph],
            name = 'ph'
        )

        data = Data([temperature_env_data, temperature_aqua_data, ph_data])

        #publish data to plotly
        plot_url = py.plot(data, filename=plot_name, fileopt='extend')

        #data print for debug
        print str(date) + ' | temp_aqua: ' + str(temp_aqua) + ' | temp_env: ' + str(temp_env) + ' | ph: ' + str(ph)




