import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *
import datetime

import sensorInterface

class plotlyInterface():

    def __init__(self):
        self.dummy = 0
        #self.username = None
        #self.api_key = None
        #self.setup()

    def check_file(self):
        import os
        import os.path

        PATH='/root/.plotly/.credentials'

        print 'checking file'

        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
            print "File exists and is readable"

            f = open(PATH)
            lines = f.readlines()
            f.close()
            print 'file content: '
            print lines

            return 0

        else:
            print "Either file is missing or is not readable"
            return -1

    def setup(self):
        #check file
        f = self.check_file()

        #if success checking file
        if f == 0:
            print 'ler ficheiro autenticacao'
            my_cred = tls.get_credentials_file()
            print my_cred
            if (my_cred['username'] != '' ) and  (my_cred['api_key'] != '') :
                print 'inicio de autenticacao'

                t=py.sign_in(my_cred['username'], my_cred['api_key'])
                print 'resultado autenticaco: '+ str(t)
                if t is None:
                    print 'autenticacao concluida com sucesso'
                    return 0
                else:
                    print '!!! ERRO de autenticacao'
                    return -1
            else:
                print '!!! ERRO a ler ficheiro de autenticacao plotly - pelo menos um dos campos esta vazio'
                return -1

    def plotData_extend(self, plot_name):

        #get current time
        date = datetime.datetime.now()
        date = date.replace(microsecond=0)

        #instanciate a sensor object
        my_sens = sensorInterface.sensor()

        #get data from sensors
        print 'starting get data from sensors'
        temp_aqua = my_sens.get_temp_aqua()
        temp_env = my_sens.get_temp_env()
        ph = my_sens.get_ph()

        #data print for debug
        print 'data to print: ' + str(date) + ' | temp_aqua: ' + str(temp_aqua) + ' | temp_env: ' + str(temp_env) + ' | ph: ' + str(ph)



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
        t=self.setup() #authentication
        if t==0:
            print 'publishing data...'
            plot_url = py.plot(data, filename=plot_name, fileopt='extend')
            print plot_url

        else:
            print '!!! ERRO de autenticacao: ' + str(t)
