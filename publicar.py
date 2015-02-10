def get_temp_aqua():
    import random
    return round(random.randrange(24,26),1)

def get_temp_env():
    import random
    return round(random.randrange(18,21),1)

def get_ph():
    import random
    return round(random.random() + 6.0,1)


def publica_plot():
    import datetime

    import plotly.plotly as py
    import plotly.tools as tls
    from plotly.graph_objs import *

    #log in
    my_cred = tls.get_credentials_file()
    py.sign_in(my_cred['username'], my_cred['api_key'])

    #get data
    date = datetime.datetime.now()
    temp_aqua = get_temp_aqua()
    temp_env = get_temp_env()
    ph = get_ph()

    temperature_env_data = Scatter(
        y=[temp_env],
        x=[date],
        name = 'temperatura ambiente'
    )

    temperature_aqua_data = Scatter(
        y=[temp_aqua],
        x=[date],
        name = 'temperatura aquario'
    )

    ph_data = Scatter(
        x = [date],
        y = [ph],
        name = 'ph'
    )

    data = Data([temperature_env_data, temperature_aqua_data, ph_data])

    #publicar dados
    plot_url = py.plot(data, filename='temperature', fileopt='extend')

    #print de controlo
    print str(date) + ' | temp_aqua: ' + str(temp_aqua) + ' | temp_env: ' + str(temp_env) + ' | ph: ' + str(ph)


class Publicar:
    # def __init__(self):
    #     self.nome = 'ptsaraiva'

    def publica_n(self):
        print ('teste publica')
        return 0
