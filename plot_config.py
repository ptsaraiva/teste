import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *
import datetime


my_cred = tls.get_credentials_file()
py.sign_in(my_cred['username'], my_cred['api_key'])

data = Data([
    Scatter(
        x=[],
        y=[]
    )
])


#t0 = (datetime.datetime.now() - datetime.timedelta(days = 3)).replace(minute=0,second=0,microsecond=0)
t0 = (datetime.datetime.now() - datetime.timedelta(days = 3))
t1 = datetime.datetime.now()
print (t0)
print (t1)

t0=int(t0.strftime('%s'))*1000
t1=int(t1.strftime('%s'))*1000
print (t0)
print (t1)


layout = Layout(xaxis = XAxis(range=[t0,t1], autorange = False ),yaxis = YAxis (autorange = True ))

fig=Figure(data= data, layout = layout)
plot_url = py.plot(fig,filename = 'temperature', fileopt='extend')